// Firebase Configuration
// Get these values from your Firebase Console: https://console.firebase.google.com

const firebaseConfig = {
  apiKey: "AIzaSyCDOYDjX7aUYZK3Cc12QfbJ2a3R4wX9N6w",
  authDomain: "javalearn-215ab.firebaseapp.com",
  projectId: "javalearn-215ab",
  storageBucket: "javalearn-215ab.firebasestorage.app",
  messagingSenderId: "80118598522",
  appId: "1:80118598522:web:bb1525ff04a40bd41d64c3"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get references to Firebase services
const auth = firebase.auth();
const db = firebase.firestore();

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { auth, db };
}
