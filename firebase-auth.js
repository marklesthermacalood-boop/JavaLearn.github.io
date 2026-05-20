// Firebase Authentication Handler

// Check if user is logged in and redirect appropriately
firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    localStorage.setItem("userId", user.uid);
    localStorage.setItem("userEmail", user.email);
    // User is signed in
    console.log("User logged in:", user.email);
  } else {
    localStorage.removeItem("userId");
    localStorage.removeItem("userEmail");
    // User is signed out
    console.log("User logged out");
  }
});

// ===== REGISTRATION =====
async function handleSignUp(email, password, username) {
  try {
    // Create user account
    const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
    const user = userCredential.user;

    // Update user profile with username
    await user.updateProfile({
      displayName: username
    });

    // Create user document in Firestore (use server timestamp)
    await db.collection("users").doc(user.uid).set({
      uid: user.uid,
      email: email,
      username: username,
      role: "student",
      createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      scores: []
    });

    console.log("User registered successfully:", user.email);
    return { success: true, user: user };
  } catch (error) {
    console.error("Registration error:", error.message);
    return { success: false, error: error.message };
  }
}

// ===== LOGIN =====
async function handleLogin(email, password) {
  try {
    const userCredential = await firebase.auth().signInWithEmailAndPassword(email, password);
    const user = userCredential.user;
    console.log("User logged in:", user.email);
    return { success: true, user: user };
  } catch (error) {
    console.error("Login error:", error.message);
    return { success: false, error: error.message };
  }
}

// ===== LOGOUT =====
async function handleLogout() {
  try {
    await firebase.auth().signOut();
    console.log("User logged out");
    return { success: true };
  } catch (error) {
    console.error("Logout error:", error.message);
    return { success: false, error: error.message };
  }
}

// ===== GET CURRENT USER =====
function getCurrentUser() {
  return firebase.auth().currentUser;
}

// ===== CHECK IF USER IS AUTHENTICATED =====
function isUserAuthenticated() {
  return firebase.auth().currentUser !== null;
}

// ===== SAVE SCORE =====
async function saveScore(lessonId, challengeId, score, correct, total) {
  try {
    const user = firebase.auth().currentUser;
    if (!user) {
      return { success: false, error: "User not authenticated" };
    }

    const scoreData = {
      userId: user.uid,
      lessonId: lessonId || null,
      challengeId: challengeId || null,
      score: score,
      correct: correct,
      total: total,
      timestamp: firebase.firestore.FieldValue.serverTimestamp(),
      userEmail: user.email,
      username: user.displayName || user.email.split('@')[0]
    };

    console.log("Saving score data:", scoreData);

    // Add to Firestore
    const docRef = await db.collection("scores").add(scoreData);
    console.log("Score saved with ID:", docRef.id);

    // Also update user's scores array (use set with merge to create if doesn't exist)
    await db.collection("users").doc(user.uid).set({
      scores: firebase.firestore.FieldValue.arrayUnion(docRef.id)
    }, { merge: true });

    return { success: true, scoreId: docRef.id };
  } catch (error) {
    console.error("Error saving score:", error.message);
    return { success: false, error: error.message };
  }
}

// ===== GET USER SCORES =====
async function getUserScores() {
  try {
    const user = firebase.auth().currentUser;
    if (!user) {
      return { success: false, error: "User not authenticated" };
    }

    // Try to get scores with orderBy
    try {
      const snapshot = await db.collection("scores")
        .where("userId", "==", user.uid)
        .orderBy("timestamp", "desc")
        .get();

      const scores = [];
      snapshot.forEach((doc) => {
        scores.push({ id: doc.id, ...doc.data() });
      });

      console.log("Scores loaded successfully:", scores.length);
      return { success: true, scores: scores };
    } catch (indexError) {
      // If composite index error, try without orderBy
      console.warn("Composite index not ready, trying fallback query:", indexError.message);
      
      const snapshot = await db.collection("scores")
        .where("userId", "==", user.uid)
        .get();

      const scores = [];
      snapshot.forEach((doc) => {
        scores.push({ id: doc.id, ...doc.data() });
      });

      // Sort client-side
      scores.sort((a, b) => {
        const timeA = a.timestamp?.seconds || 0;
        const timeB = b.timestamp?.seconds || 0;
        return timeB - timeA;
      });

      console.log("Scores loaded with fallback:", scores.length);
      return { success: true, scores: scores };
    }
  } catch (error) {
    console.error("Error fetching scores:", error.message);
    return { success: false, error: error.message };
  }
}

// ===== GET LEADERBOARD =====
async function getLeaderboard(limit = 10) {
  try {
    const snapshot = await db.collection("scores")
      .orderBy("score", "desc")
      .limit(limit)
      .get();

    const leaderboard = [];
    snapshot.forEach((doc) => {
      leaderboard.push({ id: doc.id, ...doc.data() });
    });

    return { success: true, leaderboard: leaderboard };
  } catch (error) {
    console.error("Error fetching leaderboard:", error.message);
    return { success: false, error: error.message };
  }
}


