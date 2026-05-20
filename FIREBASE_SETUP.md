# Firebase Setup Guide for DSA Website

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Click **"Create a project"**
3. Name it: `dsa-website` (or your preferred name)
4. Click **Create Project**
5. Wait for initialization to complete

## Step 2: Enable Authentication

1. In Firebase Console, go to **Authentication** (left sidebar)
2. Click **Get Started**
3. Select **Email/Password** method
4. Toggle **Enable** and click **Save**

## Step 3: Create Firestore Database

1. Go to **Firestore Database** (left sidebar)
2. Click **Create Database**
3. Select **Start in test mode** (for development)
4. Choose a location closest to you
5. Click **Create**

## Step 4: Get Your Firebase Config

1. Go to **Project Settings** (gear icon, top right)
2. Under "Your apps", click the web icon `</>`
3. Copy the config object that looks like:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_ID",
  appId: "YOUR_APP_ID"
};
```

## Step 5: Update firebase-config.js

1. Open `firebase-config.js` in your project
2. Replace the placeholder values with your actual Firebase config
3. Save the file

## Step 6: Create Firestore Collections & Indexes

Your Firestore database will automatically create collections when data is added, but here's the structure:

### Collection: `users`
Stores user information:
```
{
  uid: "unique_user_id",
  email:    ,
  username: "john_doe",
  role: "student",
  createdAt: timestamp,
  scores: ["scoreId1", "scoreId2", ...]
}
```

### Collection: `scores`
Stores user scores/progress:
```
{
  userId: "unique_user_id",
  lessonId: 1 or null,
  challengeId: 5 or null,
  score: 85,
  correct: 17,
  total: 20,
  timestamp: timestamp,
  userEmail: "user@example.com",
  username: "john_doe"
}
```

## Step 7: Update HTML Files in Your Project

All your HTML files that need authentication should include:

```html
<!-- Add to <head> section -->
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-firestore.js"></script>

<script src="firebase-config.js"></script>
<script src="firebase-auth.js"></script>
```

## Step 8: Using Firebase Functions in Your Code

### Save a Score
```javascript
const result = await saveScore(lessonId, challengeId, score, correct, total);
if (result.success) {
  console.log("Score saved:", result.scoreId);
}
```

### Get User Scores
```javascript
const result = await getUserScores();
if (result.success) {
  console.log("User scores:", result.scores);
}
```

### Get Leaderboard
```javascript
const result = await getLeaderboard(10); // Top 10
if (result.success) {
  console.log("Leaderboard:", result.leaderboard);
}
```

### Check if User is Logged In
```javascript
if (isUserAuthenticated()) {
  const user = getCurrentUser();
  console.log("Logged in as:", user.email);
}
```

### Logout
```javascript
await handleLogout();
window.location.href = "login.html";
```

## Step 9: Deploy to GitHub Pages

1. Commit and push your changes:
```bash
git add .
git commit -m "Add Firebase database integration"
git push origin main
```

2. Your GitHub Pages site will automatically deploy

## Testing

1. Visit your website: `https://yourdomain.com/signup.html`
2. Create a new account
3. Login with those credentials
4. You should be redirected to dashboard
5. Check Firebase Console → Firestore to see your user data

## Production Setup (Important!)

Before going live:

1. **Update Firebase Security Rules** in Firestore:
   - Go to **Firestore** → **Rules** tab
   - Replace with:
   ```
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{userId} {
         allow read, write: if request.auth.uid == userId;
       }
       match /scores/{scoreId} {
         allow read: if request.auth != null;
         allow write: if request.auth != null && 
                      request.resource.data.userId == request.auth.uid;
       }
     }
   }
   ```

2. **Add authorized domains** in Firebase Authentication:
   - Go to **Authentication** → **Settings**
   - Add your domain: `yourdomain.com`

## Troubleshooting

### "Firebase is not defined"
- Make sure Firebase SDK scripts are loaded BEFORE firebase-config.js
- Check browser console for errors

### Authentication not working
- Clear browser cache (localStorage might have old data)
- Check Firebase Console → Authentication → Users to see if accounts exist

### Scores not saving
- Make sure user is logged in before saving
- Check browser console for error messages
- Verify Firestore rules are correct

### CORS Issues
- Firebase handles CORS automatically, no extra setup needed
- If you see CORS errors, it's likely a different issue

## Next Steps

1. Add score-saving functionality to your quiz/exercise pages
2. Create a leaderboard page
3. Add user profile page to view personal scores
4. Monitor Firestore usage in Firebase Console
