// Example: How to Save Scores from Your Quiz/Challenge/Exercise Pages

// Add these scripts to your page <head>:
/*
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore-compat.js"></script>
<script src="firebase-config.js"></script>
<script src="firebase-auth.js"></script>
*/

// Example 1: Save score after quiz completion
async function submitQuiz(lessonNumber, correctAnswers, totalQuestions) {
  if (!isUserAuthenticated()) {
    alert("Please login first!");
    window.location.href = "login.html";
    return;
  }

  const score = Math.round((correctAnswers / totalQuestions) * 100);
  
  const result = await saveScore(
    lessonNumber,      // lesson ID
    null,              // challenge ID (null for quiz)
    score,             // percentage score
    correctAnswers,    // correct count
    totalQuestions     // total count
  );

  if (result.success) {
    console.log("✅ Score saved successfully!");
    alert(`Quiz completed! Score: ${score}%`);
  } else {
    console.error("❌ Error saving score:", result.error);
    alert("Failed to save score: " + result.error);
  }
}

// Example 2: Save score after challenge
async function completeChallenge(challengeId, score, attempts) {
  if (!isUserAuthenticated()) {
    alert("Please login first!");
    window.location.href = "login.html";
    return;
  }

  const result = await saveScore(
    null,              // lesson ID (null for challenge)
    challengeId,       // challenge ID
    score,             // score
    attempts,          // correct attempts
    100                // total possible
  );

  if (result.success) {
    console.log("Challenge score saved!");
  }
}

// Example 3: Display user's scores on dashboard
async function displayUserScores() {
  if (!isUserAuthenticated()) {
    window.location.href = "login.html";
    return;
  }

  const result = await getUserScores();
  
  if (result.success) {
    const scores = result.scores;
    let html = "<h2>Your Scores</h2>";
    
    scores.forEach(score => {
      const date = new Date(score.timestamp.seconds * 1000).toLocaleDateString();
      const type = score.lessonId ? `Lesson ${score.lessonId}` : `Challenge ${score.challengeId}`;
      
      html += `
        <div style="margin: 10px 0; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
          <strong>${type}</strong> - ${score.score}% (${score.correct}/${score.total})
          <br><small>${date}</small>
        </div>
      `;
    });
    
    document.getElementById("scores-container").innerHTML = html;
  }
}

// Example 4: Display leaderboard
async function displayLeaderboard() {
  const result = await getLeaderboard(10);
  
  if (result.success) {
    const leaderboard = result.leaderboard;
    let html = "<h2>Top 10 Scorers</h2><ol>";
    
    leaderboard.forEach((entry, index) => {
      html += `
        <li>
          <strong>${entry.username}</strong> - ${entry.score}% 
          (${entry.correct}/${entry.total})
        </li>
      `;
    });
    
    html += "</ol>";
    document.getElementById("leaderboard-container").innerHTML = html;
  }
}

// Example 5: Update UI based on login status
function updateAuthUI() {
  const user = getCurrentUser();
  
  if (user) {
    // User is logged in
    document.getElementById("user-name").textContent = user.displayName || user.email;
    document.getElementById("auth-buttons").innerHTML = `
      <button onclick="handleLogout(); window.location.reload();">Logout</button>
    `;
    document.getElementById("quiz-section").style.display = "block";
  } else {
    // User is not logged in
    document.getElementById("auth-buttons").innerHTML = `
      <a href="login.html">Login</a>
      <a href="signup.html">Sign Up</a>
    `;
    document.getElementById("quiz-section").style.display = "none";
  }
}

// Call on page load
document.addEventListener("DOMContentLoaded", () => {
  firebase.auth().onAuthStateChanged((user) => {
    updateAuthUI();
    if (user) {
      displayUserScores();
      displayLeaderboard();
    }
  });
});

// Example HTML structure:
/*
<!DOCTYPE html>
<html>
<head>
  <title>Quiz</title>
  <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore-compat.js"></script>
  <script src="firebase-config.js"></script>
  <script src="firebase-auth.js"></script>
</head>
<body>
  <div id="auth-buttons"></div>
  
  <div id="quiz-section" style="display: none;">
    <h1>Quiz</h1>
    <!-- Your quiz questions here -->
    <button onclick="submitQuiz(1, 15, 20)">Submit Quiz</button>
  </div>
  
  <div id="scores-container"></div>
  <div id="leaderboard-container"></div>
  
  <script src="quiz-score-example.js"></script>
</body>
</html>
*/


