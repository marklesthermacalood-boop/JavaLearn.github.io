# Firestore Security Rules

For production, update your Firestore security rules to protect user data while allowing the app to function properly.

## How to Update Rules in Firebase Console

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project
3. Go to **Firestore Database** → **Rules** tab
4. Replace all content with the rules below
5. Click **Publish**

## Production Security Rules

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own user document
    match /users/{userId} {
      allow read, write: if request.auth.uid == userId;
    }

    // Scores are readable by anyone (for leaderboard), 
    // but only writable by the user who created them
    match /scores/{scoreId} {
      allow read: if request.auth != null;
      allow create, write: if request.auth != null && 
                            request.resource.data.userId == request.auth.uid;
      allow delete: if request.auth != null && 
                     request.resource.data.userId == request.auth.uid;
    }

    // Default: deny all other access
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

## What These Rules Do

**Users Collection:**
- ✅ Each user can read/write only their own profile
- ❌ Users cannot access other user profiles
- ❌ Anonymous users cannot access user data

**Scores Collection:**
- ✅ Authenticated users can read all scores (needed for leaderboard)
- ✅ Users can write/save their own scores
- ✅ Users can delete their own scores
- ❌ Users cannot modify or delete other users' scores
- ❌ Anonymous users cannot read or write

**Other Collections:**
- ❌ Anything not explicitly allowed is denied
- This is the "fail-secure" approach

## Testing Rules Locally (Optional)

You can test rules in Firebase Console:
1. Go to **Firestore** → **Rules** tab
2. Click **Rules Playground** at the bottom
3. Choose "Simulate read/write" to test permissions

## Authorized Domains

Before going live, add your domain to authorized list:

1. Go to **Authentication** (left sidebar)
2. Click **Settings** tab
3. Under "Authorized domains", add:
   - `yourdomain.com`
   - `www.yourdomain.com`
   - Any other domain you use

## Data Retention Policy (Optional)

You can set up automatic data deletion policies for compliance:

1. Go to **Firestore** → **Data** tab
2. Set TTL (time-to-live) policies if needed
3. Consider keeping user scores indefinitely

## Monitoring & Quotas

Free Tier Limits:
- 1 GB storage total
- 50k reads/day
- 20k writes/day
- 20k deletes/day

Monitor usage in **Firestore** → **Usage** tab

For high traffic, upgrade to Blaze (pay-as-you-go) plan.

## Troubleshooting

### "Permission denied" errors
- Check that user is authenticated
- Verify the user ID matches the document ID
- Check rules syntax in Rules Playground

### Scores not saving
- Ensure `userId` field matches authenticated user ID
- Check that scores collection exists

### Leaderboard empty
- Verify scores are being written (check Firestore Data tab)
- Make sure read permissions allow leaderboard access
