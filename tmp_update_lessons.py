from pathlib import Path

lesson_data = {
    'lesson1.html': {
        'title': 'Lesson 1: What is Java?',
        'icon': '☕',
        'breadcrumb': 'Home > Lessons > Lesson 1',
        'intro': 'Java is a powerful, platform-independent programming language used for desktop apps, mobile apps, servers, and more. It is designed to run anywhere through the Java Virtual Machine (JVM), which executes compiled Java bytecode on any supported platform.',
        'learn': [
            'Understand what makes Java portable and widely used.',
            'Learn how Java source code becomes bytecode and runs on the JVM.',
            'See the structure of a simple Java program and where execution begins.',
        ],
        'why': 'Java is used in many real-world systems from Android apps to enterprise servers. Learning Java gives you a strong foundation in programming and helps you understand how many big applications work.',
        'concepts': [
            ('Java source code', 'Human-readable code written by a developer in a .java file.'),
            ('Compilation', 'The process that turns Java code into JVM bytecode using javac.'),
            ('Bytecode', 'Platform-independent instructions executed by the JVM.'),
            ('JVM', 'Java Virtual Machine that runs bytecode on different operating systems.'),
            ('main method', 'The starting point of a Java program: public static void main(String[] args).'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    System.out.println("Hello, Java!");\n  }\n}',
        'takeaway': 'Java programs run inside the JVM and are portable across platforms because Java code is compiled into bytecode instead of machine-specific instructions.',
        'nav': '<a href="lesson2.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Change the text inside System.out.println and run the code to see how the program prints a message. Then try replacing the message with another short sentence.',
    },
    'lesson2.html': {
        'title': 'Lesson 2: Variables & Data Types',
        'icon': '🔢',
        'breadcrumb': 'Home > Lessons > Lesson 2',
        'intro': 'Variables store values that your program can use and change. Every variable has a data type, which tells Java what kind of information it holds and how much memory to reserve.',
        'learn': [
            'Learn how to declare variables and give them names.',
            'Understand Java primitive types and common reference types like String.',
            'Avoid common mistakes when using variable types and names.',
        ],
        'why': 'Using the right data types helps Java catch errors early and makes your program faster and easier to maintain.',
        'concepts': [
            ('int', 'Stores whole numbers like 42 or -10.'),
            ('double', 'Stores decimal numbers like 9.99.'),
            ('boolean', 'Stores true or false values.'),
            ('char', 'Stores a single character, such as "A".'),
            ('String', 'Stores text. Strings are objects in Java.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    String name = "Alice";\n    int age = 20;\n    double score = 95.5;\n    boolean passed = true;\n    char grade = \'A\';\n\n    System.out.println(name + " is " + age + " years old.");\n    System.out.println("Score: " + score);\n    System.out.println("Passed: " + passed);\n    System.out.println("Grade: " + grade);\n  }\n}',
        'takeaway': 'Every variable in Java has a type, and choosing the right type makes your code safer and easier to understand.',
        'nav': '<a href="lesson1.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson3.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Add a new variable for your favorite hobby and print a sentence that includes the hobby and one of your other variables.',
    },
    'lesson3.html': {
        'title': 'Lesson 3: Operators',
        'icon': '➗',
        'breadcrumb': 'Home > Lessons > Lesson 3',
        'intro': 'Operators are the tools Java uses to work with values. You can add numbers, compare values, and combine conditions to make your program solve problems.',
        'learn': [
            'Use arithmetic and comparison operators to build expressions.',
            'Combine conditions with logical operators like && and ||.',
            'See how operator order affects the result of a calculation.',
        ],
        'why': 'Operators let your code solve math problems, compare values, and decide what to do next in a program.',
        'concepts': [
            ('Arithmetic', 'Operators like +, -, *, and / for math.'),
            ('Comparison', 'Operators like ==, !=, >, and < to compare values.'),
            ('Logical', 'Operators like && and || to combine true/false conditions.'),
            ('Assignment', 'The = operator stores a value into a variable.'),
            ('Concatenation', 'Using + to join text strings.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    int a = 10;\n    int b = 4;\n    System.out.println("Add: " + (a + b));\n    System.out.println("Subtract: " + (a - b));\n    System.out.println("Multiply: " + (a * b));\n    System.out.println("Divide: " + (a / b));\n    System.out.println("Is a bigger than b? " + (a > b));\n    System.out.println("Both true? " + (a > b && b > 0));\n  }\n}',
        'takeaway': 'Operators are the building blocks for calculations, comparisons, and logic in Java programs.',
        'nav': '<a href="lesson2.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson4.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Create two number variables and print whether the first is greater than the second, then print the result of a combined comparison using && or ||.',
    },
    'lesson4.html': {
        'title': 'Lesson 4: If Statements',
        'icon': '⚡',
        'breadcrumb': 'Home > Lessons > Lesson 4',
        'intro': 'If statements let your program make choices. Java can run one set of instructions when a condition is true, and another set when it is false.',
        'learn': [
            'Use if, else if, and else to handle different conditions.',
            'Write boolean expressions that compare values.',
            'Avoid common mistakes like missing braces or wrong comparisons.',
        ],
        'why': 'Decision-making is essential for programs that respond to data, such as checking scores, validating input, or selecting options.',
        'concepts': [
            ('if', 'Runs code only when a condition is true.'),
            ('else if', 'Checks another condition when the first one is false.'),
            ('else', 'Runs code when no earlier conditions are true.'),
            ('Condition', 'A true/false test that controls which code runs.'),
            ('Boolean', 'A value that is either true or false.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    int score = 75;\n    if (score >= 90) {\n      System.out.println("Excellent");\n    } else if (score >= 60) {\n      System.out.println("Good job");\n    } else {\n      System.out.println("Keep practicing");\n    }\n\n    int temperature = 80;\n    if (temperature > 85) {\n      System.out.println("It is very hot today.");\n    } else {\n      System.out.println("The weather is moderate.");\n    }\n  }\n}',
        'takeaway': 'If statements make your Java programs smart by selecting the right action based on the data.',
        'nav': '<a href="lesson3.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson5.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Add another else-if branch to handle scores between 40 and 59 with a different message.',
    },
    'lesson5.html': {
        'title': 'Lesson 5: Loops',
        'icon': '🔁',
        'breadcrumb': 'Home > Lessons > Lesson 5',
        'intro': 'Loops let Java repeat actions automatically. They are useful for counting, processing lists, and running the same code many times without writing duplicate instructions.',
        'learn': [
            'Use for, while, and do-while loops appropriately.',
            'Process repeating tasks with fewer lines of code.',
            'Understand when to stop a loop and how to avoid infinite repetition.',
        ],
        'why': 'Loops are essential for programs that repeat work, like processing a list of values, reading input until a condition stops, or generating repeated output.',
        'concepts': [
            ('for loop', 'Repeats a fixed number of times with an index.'),
            ('while loop', 'Repeats while a condition stays true.'),
            ('do-while loop', 'Runs once, then repeats while a condition is true.'),
            ('break', 'Stops the loop immediately.'),
            ('continue', 'Skips the rest of the current loop iteration.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    for (int i = 1; i <= 5; i++) {\n      System.out.println("Count: " + i);\n    }\n\n    int i = 1;\n    while (i <= 3) {\n      System.out.println("While loop: " + i);\n      i++;\n    }\n\n    int j = 1;\n    do {\n      System.out.println("Do-while loop: " + j);\n      j++;\n    } while (j <= 2);\n  }\n}',
        'takeaway': 'Loops let your program repeat work efficiently and control repetition until a condition changes.',
        'nav': '<a href="lesson4.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson6.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Change the loop so it prints numbers from 5 down to 1, then finish by printing "Blast off!".',
    },
    'lesson6.html': {
        'title': 'Lesson 6: Methods',
        'icon': '🧩',
        'breadcrumb': 'Home > Lessons > Lesson 6',
        'intro': 'Methods organize code into named blocks that perform specific tasks. They make programs easier to read, test, and reuse by moving repeated logic into one place.',
        'learn': [
            'Define methods with parameters and return values.',
            'Call methods from main and other methods.',
            'Use methods to keep code clean and reusable.',
        ],
        'why': 'Methods help you avoid duplicate code and make it easier to change one part of the program without breaking everything else.',
        'concepts': [
            ('Method', 'A named block of code that performs a task.'),
            ('Parameter', 'A value passed into a method.'),
            ('Return type', 'The kind of value a method gives back.'),
            ('Call', 'Running a method from another part of code.'),
            ('Static', 'A method that belongs to the class rather than to an object.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    greet();\n    int sum = add(4, 6);\n    System.out.println("Sum: " + sum);\n    System.out.println("Is 7 even? " + isEven(7));\n  }\n\n  public static void greet() {\n    System.out.println("Hello from a method!");\n  }\n\n  public static int add(int x, int y) {\n    return x + y;\n  }\n\n  public static boolean isEven(int value) {\n    return value % 2 == 0;\n  }\n}',
        'takeaway': 'Methods break your program into reusable parts, making it easier to read and maintain.',
        'nav': '<a href="lesson5.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson7.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Add a new method named sayGoodbye() and call it from main so the program prints a farewell message after the sum.',
    },
    'lesson7.html': {
        'title': 'Lesson 7: Arrays',
        'icon': '📚',
        'breadcrumb': 'Home > Lessons > Lesson 7',
        'intro': 'Arrays store multiple values under one name. They let you keep ordered lists of data and process each item with loops.',
        'learn': [
            'Create arrays to store lists of values together.',
            'Access array items by index and iterate with a loop.',
            'Avoid common array mistakes like using the wrong index.',
        ],
        'why': 'Arrays are the simplest way to work with groups of values, and they are the foundation for more advanced data structures.',
        'concepts': [
            ('Array', 'A fixed-size collection of values in order.'),
            ('Index', 'The position of an item in the array, starting at 0.'),
            ('length', 'The number of items stored in the array.'),
            ('Element', 'A single value inside the array.'),
            ('Traversal', 'Visiting each item in the array with a loop.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    String[] fruits = {"Apple", "Banana", "Cherry"};\n    for (int i = 0; i < fruits.length; i++) {\n      System.out.println("Fruit " + (i + 1) + ": " + fruits[i]);\n    }\n\n    for (String fruit : fruits) {\n      System.out.println("Enjoy this fruit: " + fruit);\n    }\n  }\n}',
        'takeaway': 'Arrays let your program store and work with several values together, using indexes to find each one.',
        'nav': '<a href="lesson6.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson8.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Add a new item to the fruits array and print how many fruits there are using fruits.length.',
    },
    'lesson8.html': {
        'title': 'Lesson 8: Strings',
        'icon': '📝',
        'breadcrumb': 'Home > Lessons > Lesson 8',
        'intro': 'Strings hold text such as names, messages, and labels. Java treats strings as objects with useful methods for changing, comparing, and measuring text.',
        'learn': [
            'Create and combine strings with concatenation.',
            'Use common String methods like length(), charAt(), and equals().',
            'Avoid mistakes when comparing strings in Java.',
        ],
        'why': 'Text is everywhere in programs, from user messages to file names. Strings give you the tools to work with that text safely.',
        'concepts': [
            ('String', 'Text enclosed in double quotes.'),
            ('Concatenation', 'Joining text using the + operator.'),
            ('length()', 'Returns the number of characters in a string.'),
            ('charAt()', 'Gets the character at a specific position.'),
            ('equals()', 'Compares text correctly instead of using ==.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    String first = "Java";\n    String second = "Basics";\n    String message = first + " " + second;\n    System.out.println(message);\n    System.out.println("Length: " + message.length());\n    System.out.println("First char: " + message.charAt(0));\n    System.out.println("Same text? " + message.equals("Java Basics"));\n    System.out.println("Upper case: " + message.toUpperCase());\n  }\n}',
        'takeaway': 'Strings represent text, and Java provides methods to read, compare, and transform that text.',
        'nav': '<a href="lesson7.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson9.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Change the message string and print its length, the first character, and whether it matches another text with equals().',
    },
    'lesson9.html': {
        'title': 'Lesson 9: Classes & Objects',
        'icon': '🏗️',
        'breadcrumb': 'Home > Lessons > Lesson 9',
        'intro': 'Classes are blueprints for objects, and objects are the values your Java program works with. Object-oriented programming helps you model real things and behaviors in code.',
        'learn': [
            'Create classes with fields and constructors.',
            'Build objects with new and use methods to perform actions.',
            'Understand the relationship between classes and objects.',
        ],
        'why': 'Classes and objects help organize code into logical pieces, making larger programs easier to understand and extend.',
        'concepts': [
            ('Class', 'A blueprint that defines data and behavior.'),
            ('Object', 'A specific instance created from a class.'),
            ('Field', 'Data stored inside an object.'),
            ('Constructor', 'Initializes a new object when it is created.'),
            ('Method', 'An action the object can perform.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    Car car = new Car("Red", 2024);\n    car.showInfo();\n    car.honk();\n  }\n\n  static class Car {\n    String color;\n    int year;\n\n    Car(String color, int year) {\n      this.color = color;\n      this.year = year;\n    }\n\n    void showInfo() {\n      System.out.println("Car: " + color + " " + year);\n    }\n\n    void honk() {\n      System.out.println("Beep beep!");\n    }\n  }\n}',
        'takeaway': 'A class defines a type of object, and objects are created from that class so your program can work with real values and actions.',
        'nav': '<a href="lesson8.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="lesson10.html"><button class="btn-primary">Next Lesson →</button></a>',
        'exercise': 'Add a new field to the Car class, like doors or model, and print it inside showInfo().',
    },
    'lesson10.html': {
        'title': 'Lesson 10: Polymorphism',
        'icon': '🔄',
        'breadcrumb': 'Home > Lessons > Lesson 10',
        'intro': 'Polymorphism allows the same code to work with different kinds of objects. It makes Java programs more flexible because objects can share a common type and still behave differently.',
        'learn': [
            'Use a superclass type to refer to different subclass objects.',
            'Override methods in subclasses to change behavior.',
            'See how Java chooses the right method at runtime.',
        ],
        'why': 'Polymorphism helps you write code that works with many object types and is easier to extend when new classes are added.',
        'concepts': [
            ('Polymorphism', 'One action, many forms.'),
            ('Inheritance', 'A subclass reuses and extends a parent class.'),
            ('Override', 'A subclass changes how a method works.'),
            ('Superclass', 'The parent class shared by subclasses.'),
            ('Dynamic binding', 'Java chooses the correct method at runtime.'),
        ],
        'example': 'public class Main {\n  public static void main(String[] args) {\n    Animal animal = new Dog();\n    animal.speak();\n    animal = new Cat();\n    animal.speak();\n    animal = new Bird();\n    animal.speak();\n  }\n\n  static class Animal {\n    void speak() {\n      System.out.println("Animal sound");\n    }\n  }\n\n  static class Dog extends Animal {\n    @Override\n    void speak() {\n      System.out.println("Dog says woof");\n    }\n  }\n\n  static class Cat extends Animal {\n    @Override\n    void speak() {\n      System.out.println("Cat says meow");\n    }\n  }\n\n  static class Bird extends Animal {\n    @Override\n    void speak() {\n      System.out.println("Bird says tweet");\n    }\n  }\n}',
        'takeaway': 'Polymorphism lets you write general code that works with many object types through shared behavior.',
        'nav': '<a href="lesson9.html"><button class="btn-outline">← Previous Lesson</button></a>\n      <a href="index.html#"><button class="btn-primary">Finish Course</button></a>',
        'exercise': 'Add a new subclass that extends Animal and override speak() so it prints a different sound.',
    },
}

for filename, data in lesson_data.items():
    path = Path(filename)
    text = path.read_text(encoding='utf-8')

    hero_start = text.find('<section class="lesson-hero">')
    if hero_start == -1:
        raise ValueError(f'Hero section not found in {filename}')
    hero_end = text.find('</section>', hero_start)
    if hero_end == -1:
        raise ValueError(f'Hero closing tag not found in {filename}')
    hero_end += len('</section>')
    hero_html = f'''<section class="lesson-hero">\n  <div class="hero-content">\n    <div class="icon">{data['icon']}</div>\n    <div>\n      <h1>{data['title']}</h1>\n      <p class="breadcrumb">{data['breadcrumb']}</p>\n    </div>\n  </div>\n</section>'''
    text = text[:hero_start] + hero_html + text[hero_end:]

    content_start = text.find('<section class="lesson-content">')
    if content_start == -1:
        raise ValueError(f'Lesson-content section not found in {filename}')
    content_end = text.find('</section>', content_start)
    if content_end == -1:
        raise ValueError(f'Lesson-content closing tag not found in {filename}')
    content_end += len('</section>')
    concepts_html = ''.join([f'        <li><strong>{title}</strong> — {desc}</li>\n' for title, desc in data['concepts']])
    learn_html = ''.join([f'        <li>{item}</li>\n' for item in data['learn']])
    content_html = f'''<section class="lesson-content">\n    <div class="card intro">\n      <h2>{data['title']}</h2>\n      <p>{data['intro']}</p>\n    </div>\n\n    <div class="card">\n      <h3>What you will learn</h3>\n      <ul>\n{learn_html}      </ul>\n    </div>\n\n    <div class="card">\n      <h3>Why this matters</h3>\n      <p>{data['why']}</p>\n    </div>\n\n    <div class="card">\n      <h3>Important concepts</h3>\n      <ul>\n{concepts_html}      </ul>\n    </div>\n\n    <div class="card code-section">\n      <div class="code-header"><span>Example Code</span></div>\n      <pre>\n{data['example']}\n      </pre>\n    </div>\n\n    <div class="takeaway">\n      <div class="icon">💡</div>\n      <div>\n        <h3>Key Takeaway</h3>\n        <p>{data['takeaway']}</p>\n      </div>\n    </div>\n\n    <div class="lesson-nav">\n      {data['nav']}\n    </div>\n</section>'''
    text = text[:content_start] + content_html + text[content_end:]

    exercise_start = text.find('<div class="card exercise">')
    if exercise_start != -1:
        h2_end = text.find('</h2>', exercise_start)
        if h2_end != -1:
            insert_position = h2_end + len('</h2>')
            snippet = text[insert_position:insert_position+200]
            if data['exercise'] not in snippet:
                text = text[:insert_position] + f'\n  <p>{data["exercise"]}</p>\n' + text[insert_position:]

    path.write_text(text, encoding='utf-8')
    print(f'Updated {filename}')
