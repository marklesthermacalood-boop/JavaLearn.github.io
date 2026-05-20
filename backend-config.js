const REMOTE_BACKEND_URL = "https://your-app.onrender.com"; // Example: "https://your-app.onrender.com"

function getBackendOrigin() {
  if (window.location.protocol === "file:") {
    return "http://localhost:3000";
  }
  if (REMOTE_BACKEND_URL) {
    return REMOTE_BACKEND_URL.replace(/\/+$/, "");
  }
  return "";
}

function getRunUrl() {
  const origin = getBackendOrigin();
  return origin ? `${origin}/run` : "/run";
}

function getApiUrl(path) {
  const origin = getBackendOrigin();
  return origin ? `${origin}${path}` : path;
}
