const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");
const { exec } = require("child_process");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

const app = express();
const JWT_SECRET = "your_jwt_secret_key_change_in_production";

app.use(cors());
app.use(express.json());

const users = [];
const scores = [];

const ALLOWED_ADMIN_EMAILS = ["admin@javalearn.com"];
const DEFAULT_ADMIN = {
  id: 1,
  username: "admin",
  email: "admin@javalearn.com",
  password: bcrypt.hashSync("AdminPass123!", 10),
  role: "admin",
  created_at: new Date().toISOString(),
};

if (!users.some((user) => user.email === DEFAULT_ADMIN.email)) {
  users.push(DEFAULT_ADMIN);
}

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

function authenticateAdmin(req, res, next) {
  authenticateToken(req, res, () => {
    if (!req.user || req.user.role !== "admin") {
      return res.status(403).json({ success: false, error: "Admin access required" });
    }
    next();
  });
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

  let assignedRole = "student";
  if (role === "professor") {
    assignedRole = "professor";
  } else if (role === "admin") {
    if (ALLOWED_ADMIN_EMAILS.includes(email.toLowerCase())) {
      assignedRole = "admin";
    } else {
      return res.status(403).json({ success: false, error: "Admin role can only be created for a trusted account." });
    }
  }

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
      id: users.length + 1,
      username,
      email,
      password: hashedPassword,
      role: assignedRole,
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
    const user = users.find((item) => item.username === username || item.email === username);

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

function loadLessonFiles() {
  const files = fs.readdirSync(__dirname)
    .filter((name) => /^lesson\d+\.html$/.test(name))
    .sort((a, b) => {
      const aNum = parseInt(a.match(/lesson(\d+)\.html/)[1], 10);
      const bNum = parseInt(b.match(/lesson(\d+)\.html/)[1], 10);
      return aNum - bNum;
    });
  return files;
}

function buildLessonPage({ lessonNumber, title, intro, points, codeExample, takeaway, icon = '💻', difficulty = 'Beginner' }) {
  const previousLesson = lessonNumber > 1 ? `lesson${lessonNumber - 1}.html` : 'lessons.html';
  const nextLesson = `lesson${lessonNumber + 1}.html`;
  const pointItems = points
    .split(/\r?\n/)
    .filter((line) => line.trim())
    .map((line) => `      <li>${line.trim()}</li>`)
    .join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lesson ${lessonNumber} - ${title}</title>
  <link rel="stylesheet" href="styles.css">
  <script src="backend-config.js"></script>
</head>
<body>
<header>
  <div class="logo">⚡ JavaLearn Hub</div>
  <nav>
    <a href="index.html#">Home</a>
    <a href="lessons.html">Lessons</a>
    <a href="dashboard.html">Dashboard</a>
  </nav>
</header>

<section class="lesson-hero">
  <div class="hero-content">
    <div class="icon">${icon}</div>
    <div>
      <h1>Lesson ${lessonNumber}: ${title}</h1>
      <p class="breadcrumb">Home > Lessons > Lesson ${lessonNumber}</p>
    </div>
  </div>
</section>

<section class="lesson-content">
  <div class="card intro">
    <h2>Lesson ${lessonNumber}: ${title}</h2>
    <p>${intro}</p>
  </div>
  <div class="card">
    <h3>What you will learn</h3>
    <ul>
${pointItems}
    </ul>
  </div>
  <div class="card code-section">
    <div class="code-header"><span>Example Code</span></div>
    <pre>
${codeExample}
    </pre>
  </div>
  <div class="takeaway">
    <div class="icon">?</div>
    <div>
      <h3>Key Takeaway</h3>
      <p>${takeaway}</p>
    </div>
  </div>
  <div class="lesson-nav">
    <a href="${previousLesson}"><button class="btn-outline">← Previous Lesson</button></a>
    <a href="${nextLesson}"><button class="btn-primary">Next Lesson →</button></a>
  </div>
</section>

<div class="card exercise">
  <h2>Java Compiler</h2>
  <textarea id="code">${codeExample}</textarea>
  <button onclick="runCode()" class="btn-primary">Run Code</button>
  <button onclick="resetCode()" class="btn-primary">Reset Code</button>
  <div id="status" class="status"></div>
  <pre id="output"></pre>
</div>

<script>
function getRunUrlSafe() {
  return typeof getRunUrl === 'function' ? getRunUrl() : '/run';
}

async function runCode() {
  const code = document.getElementById('code').value;
  const output = document.getElementById('output');
  const status = document.getElementById('status');

  try {
    const runUrl = getRunUrlSafe();
    const response = await fetch(runUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    });

    let result;
    const contentType = response.headers.get('content-type') || '';
    if (!response.ok) {
      const text = await response.text();
      throw new Error(text || ('Server returned ' + response.status));
    }
    if (contentType.includes('application/json')) {
      result = await response.json();
    } else {
      const text = await response.text();
      throw new Error(text || 'Server returned non-JSON response');
    }

    if (!result.success) {
      status.textContent = '❌ Code failed to compile or run.';
      status.className = 'status error';
      output.innerText = result.error;
      return;
    }

    status.textContent = '✅ Success!';
    status.className = 'status success';
    output.innerText = result.output;
  } catch (err) {
    status.textContent = '❌ Server error.';
    status.className = 'status error';
    output.innerText = err.message;
  }
}

function resetCode() {
  document.getElementById('code').value = \`${codeExample}\`;
  document.getElementById('output').innerText = '';
  document.getElementById('status').textContent = '';
  document.getElementById('status').className = 'status';
}
</script>

<footer>
  © 2025 JavaLearn Hub. All rights reserved.
</footer>
</body>
</html>`;
}

app.get("/api/admin/lessons", (req, res) => {
  try {
    const files = loadLessonFiles();
    const lessons = files.map((file) => {
      const content = fs.readFileSync(path.join(__dirname, file), 'utf8');
      const titleMatch = content.match(/<h1>([^<]+)<\/h1>/);
      const title = titleMatch ? titleMatch[1] : file;
      const introMatch = content.match(/<div class="card intro">[\s\S]*?<p>([\s\S]*?)<\/p>/);
      const intro = introMatch ? introMatch[1].trim() : '';
      const codeMatch = content.match(/<div class="card code-section">[\s\S]*?<pre>\n([\s\S]*?)\n    <\/pre>/);
      const codeExample = codeMatch ? codeMatch[1].trim() : '';
      const takeawayMatch = content.match(/<div class="takeaway">[\s\S]*?<p>([\s\S]*?)<\/p>/);
      const takeaway = takeawayMatch ? takeawayMatch[1].trim() : '';
      const pointsMatch = content.match(/<h3>What you will learn<\/h3>[\s\S]*?<ul>([\s\S]*?)<\/ul>/);
      const points = pointsMatch ? pointsMatch[1].replace(/<li>|<\/li>/g, '').split(/\r?\n/).map((line) => line.trim()).filter(Boolean).join('\n') : '';
      const number = parseInt(file.match(/lesson(\d+)\.html/)[1], 10);
      return { file, lessonNumber: number, title, intro, points, codeExample, takeaway };
    });
    res.json({ success: true, lessons });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

app.post("/api/admin/lessons/:lessonNumber", (req, res) => {
  try {
    const lessonNumber = parseInt(req.params.lessonNumber, 10);
    const { title, intro, points, codeExample, takeaway } = req.body;
    if (!title || !intro || !points || !codeExample || !takeaway) {
      return res.status(400).json({ success: false, error: 'Missing required lesson fields.' });
    }
    const lessonHtml = buildLessonPage({ lessonNumber, title, intro, points, codeExample, takeaway });
    const filePath = path.join(__dirname, `lesson${lessonNumber}.html`);
    fs.writeFileSync(filePath, lessonHtml, 'utf8');
    res.json({ success: true, file: `lesson${lessonNumber}.html` });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
});

app.use(express.static(__dirname));

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});



