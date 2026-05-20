const express = require("express");
const cors = require("cors");
const fs = require("fs");
const { exec } = require("child_process");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const app = express();
const JWT_SECRET = "your_jwt_secret_key_change_in_production";

app.use(cors());
app.use(express.json());

const users = [];
const scores = [];

function authenticateToken(req, res, next) {
  const token = req.headers["authorization"]?.split(" ")[1];

  if (!token) {
    return res.status(401).json({ success: false, error: "No token provided" });
  }

  try {
    const user = jwt.verify(token, JWT_SECRET);
    req.user = user;
    next();
  } catch (err) {
    res.status(403).json({ success: false, error: "Invalid token" });
  }
}

function checkExistingScore(user_id, lesson_id, challenge_id) {
  return scores.find(
    (item) =>
      item.user_id === user_id &&
      item.lesson_id === (lesson_id || null) &&
      item.challenge_id === (challenge_id || null)
  );
}

// ===== AUTH ENDPOINTS =====

app.post("/api/auth/register", async (req, res) => {
  const { username, email, password, role = "student" } = req.body;

  if (!username || !email || !password) {
    return res.status(400).json({ success: false, error: "Missing required fields" });
  }

  if (users.some((user) => user.username === username || user.email === email)) {
    return res.status(409).json({ success: false, error: "User already exists" });
  }

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
      id: users.length + 1,
      username,
      email,
      password: hashedPassword,
      role,
      created_at: new Date().toISOString(),
    };

    users.push(newUser);

    res.json({ success: true, message: "User registered successfully" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

app.post("/api/auth/login", async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ success: false, error: "Missing username or password" });
  }

  try {
    const user = users.find((item) => item.username === username);

    if (!user) {
      return res.status(401).json({ success: false, error: "Invalid credentials" });
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      return res.status(401).json({ success: false, error: "Invalid credentials" });
    }

    const token = jwt.sign(
      { id: user.id, username: user.username, role: user.role },
      JWT_SECRET,
      { expiresIn: "24h" }
    );

    res.json({
      success: true,
      message: "Login successful",
      token,
      user: { id: user.id, username: user.username, email: user.email, role: user.role },
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

// ===== SCORE ENDPOINTS =====

app.post("/api/scores/save", authenticateToken, async (req, res) => {
  const { lesson_id, challenge_id, score, max_score = 100 } = req.body;
  const user_id = req.user.id;

  if (!lesson_id && !challenge_id) {
    return res.status(400).json({ success: false, error: "lesson_id or challenge_id required" });
  }

  try {
    const existing = checkExistingScore(user_id, lesson_id, challenge_id);

    if (existing) {
      existing.score = score;
      existing.max_score = max_score;
      existing.completed = true;
      existing.completed_at = new Date().toISOString();
    } else {
      scores.push({
        id: scores.length + 1,
        user_id,
        lesson_id: lesson_id || null,
        challenge_id: challenge_id || null,
        score,
        max_score,
        completed: true,
        created_at: new Date().toISOString(),
        completed_at: new Date().toISOString(),
      });
    }

    res.json({ success: true, message: "Score saved" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

app.get("/api/scores/user", authenticateToken, async (req, res) => {
  const user_id = req.user.id;

  try {
    const userScores = scores
      .filter((item) => item.user_id === user_id)
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    res.json({ success: true, scores: userScores });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

app.get("/api/user/profile", authenticateToken, async (req, res) => {
  const user_id = req.user.id;

  try {
    const user = users.find((item) => item.id === user_id);

    if (!user) {
      return res.status(404).json({ success: false, error: "User not found" });
    }

    const userScores = scores.filter((item) => item.user_id === user_id && item.completed);
    const totalCompleted = userScores.length;
    const totalScore = userScores.reduce((sum, item) => sum + item.score, 0);
    const avgScore = userScores.length ? totalScore / userScores.length : 0;

    res.json({
      success: true,
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
        role: user.role,
        created_at: user.created_at,
      },
      stats: {
        total_completed: totalCompleted,
        total_score: totalScore,
        avg_score: avgScore,
      },
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ success: false, error: err.message });
  }
});

// ===== JAVA COMPILER ENDPOINT =====

app.options("/run", cors());
app.all("/run", (req, res, next) => {
  if (req.method !== "POST") {
    return res.status(405).json({
      success: false,
      error: "Method not allowed. Use POST with a JSON payload.",
    });
  }
  next();
});

app.post("/run", (req, res) => {
  const code = req.body.code;

  if (!code) {
    return res.json({ success: false, error: "No code received" });
  }

  try {
    fs.writeFileSync("Main.java", code, "utf8");
  } catch (e) {
    return res.json({ success: false, error: "Failed to write file: " + e.message });
  }

  const runOptions = { cwd: __dirname, timeout: 10000, maxBuffer: 1024 * 1024 };

  exec("javac Main.java", runOptions, (err, stdout, stderr) => {
    if (err) {
      const message = stderr?.trim() || err.message || "Compile error";
      return res.json({ success: false, error: message });
    }

    exec("java -cp . Main", runOptions, (err2, stdout2, stderr2) => {
      if (err2) {
        const message = stderr2?.trim() || err2.message || "Runtime error";
        return res.json({ success: false, error: message });
      }

      return res.json({ success: true, output: stdout2?.trim() || "No output" });
    });
  });
});

app.use(express.static(__dirname));

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});

