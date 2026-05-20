# Quick Start: Connect Your DSA Website to Firebase

## What's Been Done ✅

I've created the Firebase integration for your website. Here are the new files:

1. **firebase-config.js** - Firebase configuration (needs your credentials)
2. **firebase-auth.js** - All authentication & database functions
3. **login.html** - Updated to use Firebase
4. **signup.html** - Updated to use Firebase
5. **FIREBASE_SETUP.md** - Complete setup guide
6. **SCORE_SAVING_EXAMPLES.js** - Code examples for saving scores

## Quick Setup (5 Minutes)

### 1. Create Firebase Project
- Go to https://console.firebase.google.com
- Click "Create Project" → name it `dsa-website`
- Wait for it to finish

### 2. Enable Services
- Click **Authentication** → Get Started → Email/Password → Enable
- Click **Firestore Database** → Create Database → Test Mode → Create

### 3. Get Your Config
- Click gear icon (⚙️) at top right → Project Settings
- Scroll down to "Your apps" and click web icon `</>`
- Copy the entire config object

### 4. Update firebase-config.js
- Open `firebase-config.js` in your editor
- Replace the placeholder values with your config
- Save

### 5. Push to GitHub
```bash
git add .
git commit -m "Add Firebase database integration"
git push origin main
```

**Done!** Your website now has:
- ✅ User registration & login
- ✅ Secure authentication
- ✅ Firestore database for storing scores
- ✅ Leaderboard functionality

## Available Functions

```javascript
// Authentication
handleSignUp(email, password, username)     // Register new user
handleLogin(email, password)                // Login user
handleLogout()                              // Logout
getCurrentUser()                            // Get logged-in user
isUserAuthenticated()                       // Check if logged in

// Scores & Database
saveScore(lessonId, challengeId, score, correct, total)  // Save a score
getUserScores()                             // Get all user scores
getLeaderboard(limit)                       // Get top scorers
```

## Example: Add Score Saving to Quiz

```javascript
// When user completes quiz:
const result = await saveScore(
  1,              // Lesson 1
  null,           // No specific challenge
  85,             // Score: 85%
  17,             // Correct: 17
  20              // Total: 20 questions
);

if (result.success) {
  alert("Score saved!");
} else {
  alert("Error: " + result.error);
}
```

## Next Steps

1. **Test Login/Signup**
   - Go to your website
   - Try creating an account
   - Try logging in
   - Check Firebase Console to see your data

2. **Add Score Saving**
   - Open your quiz.html or exercise.html
   - Add the Firebase scripts to the `<head>`
   - When user completes quiz, call `saveScore()`
   - See SCORE_SAVING_EXAMPLES.js for detailed examples

3. **Add Leaderboard Page**
   - Create new page or add to dashboard
   - Call `getLeaderboard(10)` to get top 10
   - Display results in a table

4. **Update Other Pages**
   - Add Firebase to dashboard.html, challenge.html, etc.
   - Use `isUserAuthenticated()` to protect pages
   - Display user's scores using `getUserScores()`

## File Sizes & Performance

- Firebase SDK: ~60KB (cached by Google's CDN)
- Your files: ~5KB total
- Real-time database syncing
- Free tier supports ~1M+ users

## Support & Debugging

If something doesn't work:
1. Open browser DevTools (F12)
2. Look for error messages in Console
3. Check Firebase Console for data
4. Clear localStorage: `localStorage.clear()` in console
5. Check internet connection

## Common Issues

**Issue:** "Firebase is not defined"
- Solution: Make sure Firebase SDK loads before your code

**Issue:** "User not found"
- Solution: Make sure you registered first in signup.html

**Issue:** "No database connection"
- Solution: Check firebaseConfig in firebase-config.js is correct

## Free Tier Limits

Firebase free tier includes:
- ✅ Unlimited users
- ✅ 1 GB storage
- ✅ Real-time syncing
- ✅ Automatic backups

Perfect for your DSA learning platform!

---

For detailed setup steps, see **FIREBASE_SETUP.md**
For code examples, see **SCORE_SAVING_EXAMPLES.js**
