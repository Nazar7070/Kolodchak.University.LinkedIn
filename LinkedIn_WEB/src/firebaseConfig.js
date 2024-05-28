// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCvWLn9uCOd4tByCRkcdxjxrrRpGiNh6V8",
  authDomain: "linkedin-clone-371e4.firebaseapp.com",
  projectId: "linkedin-clone-371e4",
  storageBucket: "linkedin-clone-371e4.appspot.com",
  messagingSenderId: "1067296132134",
  appId: "1:1067296132134:web:7941346787ad5fcc00eae7",
  measurementId: "G-Z46SWYDKMZ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);
const storage = getStorage(app);
const analytics = getAnalytics(app);

export { app, auth, firestore, storage, analytics };
