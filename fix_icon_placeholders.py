from pathlib import Path

icon_map = {
    'lesson1.html': '☕',
    'lesson2.html': '🔢',
    'lesson3.html': '➗',
    'lesson4.html': '⚡',
    'lesson5.html': '🔁',
    'lesson6.html': '🧩',
    'lesson7.html': '📚',
    'lesson8.html': '📝',
    'lesson9.html': '🏗️',
    'lesson10.html': '🔄',
}

for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    new_text = text

    new_text = new_text.replace('??JavaLearn Hub', '☕ JavaLearn Hub')
    new_text = new_text.replace('? JavaLearn Hub', '☕ JavaLearn Hub')

    if path.name == 'index.html':
        new_text = new_text.replace('<div class="icon">??</div>\n      Lesson 1: What is Java?</a>', '<div class="icon">☕</div>\n      Lesson 1: What is Java?</a>')
        new_text = new_text.replace('<div class="icon">??</div>\n      Lesson 2: Variables & Data Types</a>', '<div class="icon">🔢</div>\n      Lesson 2: Variables & Data Types</a>')
        new_text = new_text.replace('<div class="icon">??</div>\n      Lesson 3: Operators</a>', '<div class="icon">➗</div>\n      Lesson 3: Operators</a>')
        new_text = new_text.replace('<div class="icon">??</div>\n      View All Lessons</a>', '<div class="icon">📚</div>\n      View All Lessons</a>')
    if path.name == 'lessons.html':
        new_text = new_text.replace('<h1>?? Java Lessons</h1>', '<h1>📘 Java Lessons</h1>')
    if path.name == 'dashboard.html':
        new_text = new_text.replace('<div class="icon">??</div>', '<div class="icon">📊</div>', 1)
        new_text = new_text.replace('<h2>?? Recent Scores</h2>', '<h2>🏆 Recent Scores</h2>')
        new_text = new_text.replace('`?? Lesson ${score.lessonId}`', '`📘 Lesson ${score.lessonId}`')
        new_text = new_text.replace('`?? Challenge ${score.challengeId}`', '`⚔️ Challenge ${score.challengeId}`')
    new_text = new_text.replace('messageDiv.textContent = "?? Please fill in all fields!"', 'messageDiv.textContent = "⚠️ Please fill in all fields!"')
    new_text = new_text.replace('messageDiv.textContent = "?? Password must be at least 6 characters!"', 'messageDiv.textContent = "⚠️ Password must be at least 6 characters!"')
    new_text = new_text.replace('<div class="icon">??</div>', '<div class="icon">☕</div>')

    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f'Patched {path.name}')
