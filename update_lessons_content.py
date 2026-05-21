from pathlib import Path

lessons = {
    'lesson1.html': {
        'title': 'Lesson 1: What is Java?',
        'icon': '☕',
        'breadcrumb': 'Home > Lessons > Lesson 1',
        'intro': 'Java is a popular programming language with strong support for portability, reliability, and performance. It runs on many platforms because Java programs are compiled to bytecode that can execute inside the Java Virtual Machine (JVM).',
        'learn': [
            'How Java code is written, compiled, and executed.',
            'What makes Java platform-independent, and why that matters.',
            'The role of the JVM, JRE, and JDK in Java development.',
            'How Java differs from languages that compile directly to machine code.',
        ],
        'why': 'Java is used in web applications, Android apps, enterprise systems, and desktop tools. Learning Java gives you a foundation for writing robust applications and understanding many software systems.',
        'concepts': [
            ('Java source code', 'Lines of code saved in .java files, written by developers.'),
            ('Compilation', 'Translating source code into bytecode using the Java compiler.'),
            ('Bytecode', 'Platform-neutral Java instructions that run on the JVM.'),
            ('JVM', 'Java Virtual Machine that executes bytecode on different platforms.'),
            ('main method', 'The entry point of most Java programs: public static void main(String[] args).'),
        ],
        'common': [
            'Confusing Java source code with bytecode; Java programs must be compiled first.',
            'Thinking Java runs directly on hardware instead of inside the JVM.',
            'Assuming all Java files are executable without compiling them.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    System.out.println("Java is running!");
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    System.out.println("Java is running!");
  }
}''',
        'exercise': 'Update the message in System.out.println to describe your favorite programming topic. Then run the program to see the output change.',
    },
    'lesson2.html': {
        'title': 'Lesson 2: Variables & Data Types',
        'icon': '🔢',
        'breadcrumb': 'Home > Lessons > Lesson 2',
        'intro': 'Variables hold values such as numbers, text, or true/false flags. Every variable in Java has a type that determines what values it can store and how the computer treats it.',
        'learn': [
            'How to declare and initialize variables in Java.',
            'The difference between primitive types and reference types.',
            'Common Java data types for numbers, text, and booleans.',
            'Why proper naming and typing makes code easier to read and debug.',
        ],
        'why': 'Using the correct data type prevents errors and makes your code more efficient. Java relies on types to check correctness during compilation.',
        'concepts': [
            ('int', 'Whole numbers like 42 or -7.'),
            ('double', 'Floating-point numbers such as 3.14.'),
            ('boolean', 'true or false values used in logic.'),
            ('char', 'A single character like "A" or "9".'),
            ('String', 'Text values stored as objects, like "Hello".'),
        ],
        'common': [
            'Assigning a text value to an int variable and expecting it to work.',
            'Using = instead of == when comparing values in conditions.',
            'Choosing unclear variable names like x or temp for important data.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    String name = "Alex";
    int age = 21;
    double score = 88.5;
    boolean passed = true;
    char grade = 'A';

    System.out.println(name + " is " + age + " years old.");
    System.out.println("Score: " + score);
    System.out.println("Passed: " + passed);
    System.out.println("Grade: " + grade);
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    String name = "Alex";
    int age = 21;
    double score = 88.5;
    boolean passed = true;
    char grade = 'A';

    System.out.println(name + " is " + age + " years old.");
    System.out.println("Score: " + score);
    System.out.println("Passed: " + passed);
    System.out.println("Grade: " + grade);
  }
}''',
        'exercise': 'Add a new variable for your favorite hobby or game, then print a sentence using the new variable and one of the existing variables.',
    },
    'lesson3.html': {
        'title': 'Lesson 3: Operators',
        'icon': '➗',
        'breadcrumb': 'Home > Lessons > Lesson 3',
        'intro': 'Operators are symbols that perform actions on values, like adding numbers, comparing values, or combining text. They are the building blocks for expressions in Java.',
        'learn': [
            'Use arithmetic operators to calculate values.',
            'Compare values using relational operators.',
            'Combine boolean expressions with logical operators.',
            'Concatenate text using the + operator.',
        ],
        'why': 'Operators let your program solve problems, make decisions, and transform values. They appear in nearly every line of Java code.',
        'concepts': [
            ('+', 'Adds numbers or combines text strings.'),
            ('-', 'Subtracts numbers.'),
            ('*', 'Multiplies numbers.'),
            ('/', 'Divides numbers.'),
            ('%', 'Remainder operator used for tasks like checking even/odd numbers.'),
        ],
        'common': [
            'Using == to compare Strings instead of .equals().',
            'Forgetting parentheses when combining arithmetic and text concatenation.',
            'Dividing integers and expecting a decimal result instead of truncation.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    int a = 10;
    int b = 4;
    System.out.println("Add: " + (a + b));
    System.out.println("Subtract: " + (a - b));
    System.out.println("Multiply: " + (a * b));
    System.out.println("Divide: " + (a / b));
    System.out.println("Remainder: " + (a % b));
    System.out.println("a is greater than b: " + (a > b));
    System.out.println("Both true: " + (a > b && b > 0));
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    int a = 10;
    int b = 4;
    System.out.println("Add: " + (a + b));
    System.out.println("Subtract: " + (a - b));
    System.out.println("Multiply: " + (a * b));
    System.out.println("Divide: " + (a / b));
    System.out.println("Remainder: " + (a % b));
    System.out.println("a is greater than b: " + (a > b));
    System.out.println("Both true: " + (a > b && b > 0));
  }
}''',
        'exercise': 'Change the values of a and b. Then add a new expression that checks whether a is divisible by b.',
    },
    'lesson4.html': {
        'title': 'Lesson 4: If Statements',
        'icon': '⚡',
        'breadcrumb': 'Home > Lessons > Lesson 4',
        'intro': 'If statements allow your program to make choices based on conditions. Java checks whether a condition is true, then runs the matching block of code.',
        'learn': [
            'Write if, else if, and else blocks for decision making.',
            'Build boolean conditions using comparison operators.',
            'Use nested if statements for more than one decision.',
            'Recognize when to use else if versus separate if statements.',
        ],
        'why': 'Decision-making is essential when programs need to respond differently to different data, such as checking passwords, scoring tests, or validating input.',
        'concepts': [
            ('if', 'Runs a block of code only when a condition is true.'),
            ('else if', 'Checks another condition when the first one is false.'),
            ('else', 'Runs a block when no previous condition is true.'),
            ('Condition', 'A Boolean expression that evaluates to true or false.'),
            ('Short-circuit logic', 'With && and ||, Java may skip checking the second part of a condition.'),
        ],
        'common': [
            'Using = instead of == in a condition.',
            'Forgetting braces {} around multi-line if code blocks.',
            'Writing overlapping conditions that never run the later branch.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    int score = 75;
    if (score >= 90) {
      System.out.println("Excellent");
    } else if (score >= 70) {
      System.out.println("Good job");
    } else {
      System.out.println("Keep practicing");
    }

    int temperature = 80;
    if (temperature > 95) {
      System.out.println("It is very hot.");
    } else if (temperature >= 70) {
      System.out.println("The weather is warm.");
    } else {
      System.out.println("It is cooler today.");
    }
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    int score = 75;
    if (score >= 90) {
      System.out.println("Excellent");
    } else if (score >= 70) {
      System.out.println("Good job");
    } else {
      System.out.println("Keep practicing");
    }

    int temperature = 80;
    if (temperature > 95) {
      System.out.println("It is very hot.");
    } else if (temperature >= 70) {
      System.out.println("The weather is warm.");
    } else {
      System.out.println("It is cooler today.");
    }
  }
}''',
        'exercise': 'Add another else-if branch to handle scores between 50 and 69 with a different message.',
    },
    'lesson5.html': {
        'title': 'Lesson 5: Loops',
        'icon': '🔁',
        'breadcrumb': 'Home > Lessons > Lesson 5',
        'intro': 'Loops repeat actions automatically, so you do not need to write the same code over and over. Java offers several loop types for different repetition needs.',
        'learn': [
            'Use for, while, and do-while loops to repeat code.',
            'Control loops with counters and conditions.',
            'Avoid infinite loops by managing the stop condition.',
            'Use break and continue to control loop flow.',
        ],
        'why': 'Loops are used in almost every program to process lists, repeat calculations, or wait until a condition changes.',
        'concepts': [
            ('for loop', 'Runs a fixed number of times with a loop variable.'),
            ('while loop', 'Repeats while a condition remains true.'),
            ('do-while loop', 'Runs at least once before checking the condition.'),
            ('break', 'Stops the loop immediately.'),
            ('continue', 'Skips the rest of the current loop iteration.'),
        ],
        'common': [
            'Forgetting to update the loop counter and causing an infinite loop.',
            'Using the wrong condition so the loop never starts or never ends.',
            'Breaking out of the loop too early and missing important work.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    for (int i = 1; i <= 5; i++) {
      System.out.println("Count: " + i);
    }

    int i = 1;
    while (i <= 3) {
      System.out.println("While loop: " + i);
      i++;
    }

    int j = 1;
    do {
      System.out.println("Do-while loop: " + j);
      j++;
    } while (j <= 2);
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    for (int i = 1; i <= 5; i++) {
      System.out.println("Count: " + i);
    }

    int i = 1;
    while (i <= 3) {
      System.out.println("While loop: " + i);
      i++;
    }

    int j = 1;
    do {
      System.out.println("Do-while loop: " + j);
      j++;
    } while (j <= 2);
  }
}''',
        'exercise': 'Change the for loop so it prints numbers from 5 down to 1, then print "Blast off!" after the loop.',
    },
    'lesson6.html': {
        'title': 'Lesson 6: Methods',
        'icon': '🧩',
        'breadcrumb': 'Home > Lessons > Lesson 6',
        'intro': 'Methods are reusable blocks of code that perform a specific task. They make programs easier to organize, test, and maintain by moving logic into named functions.',
        'learn': [
            'Declare methods with names, parameters, and return types.',
            'Call methods from main and pass values between them.',
            'Use methods to avoid repeating code.',
            'Understand the difference between void and non-void methods.',
        ],
        'why': 'Methods help break programs into smaller tasks, making the code easier to read and change. They are central to writing good Java applications.',
        'concepts': [
            ('Method', 'A named block of code that can be reused.'),
            ('Parameter', 'A value given to a method when it is called.'),
            ('Return type', 'The type of value a method sends back. void means no value.'),
            ('Call', 'Using a method name to execute its code.'),
            ('Static', 'A method that belongs to the class instead of an object.'),
        ],
        'common': [
            'Putting code in main instead of using methods for repeated tasks.',
            'Using the wrong return type for the value a method sends back.',
            'Forgetting to call a method after writing it.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    greet();
    int sum = add(4, 6);
    System.out.println("Sum: " + sum);
    System.out.println("Is 7 even? " + isEven(7));
  }

  public static void greet() {
    System.out.println("Hello from a method!");
  }

  public static int add(int x, int y) {
    return x + y;
  }

  public static boolean isEven(int value) {
    return value % 2 == 0;
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    greet();
    int sum = add(4, 6);
    System.out.println("Sum: " + sum);
    System.out.println("Is 7 even? " + isEven(7));
  }

  public static void greet() {
    System.out.println("Hello from a method!");
  }

  public static int add(int x, int y) {
    return x + y;
  }

  public static boolean isEven(int value) {
    return value % 2 == 0;
  }
}''',
        'exercise': 'Add a new method named sayGoodbye() and call it from main so the program prints a farewell message after the sum.',
    },
    'lesson7.html': {
        'title': 'Lesson 7: Arrays',
        'icon': '📚',
        'breadcrumb': 'Home > Lessons > Lesson 7',
        'intro': 'Arrays store multiple values in one variable. They keep values in order and let you access each item by its position number, called an index.',
        'learn': [
            'Create arrays to hold lists of values.',
            'Access array elements by index.',
            'Use loops to process every element in an array.',
            'Understand array length and valid indexes.',
        ],
        'why': 'Arrays are the simplest way to work with groups of values in Java. They are essential when you need to store multiple items together.',
        'concepts': [
            ('Array', 'A fixed-size sequence of values.'),
            ('Index', 'The position of an item in the array, starting at 0.'),
            ('length', 'The number of items in the array.'),
            ('Element', 'A single item inside an array.'),
            ('Traversal', 'Visiting array elements one by one with a loop.'),
        ],
        'common': [
            'Using an index that is too large or negative and getting an error.',
            'Assuming arrays grow automatically; they have a fixed size once created.',
            'Forgetting that the first element begins at index 0.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    String[] fruits = {"Apple", "Banana", "Cherry"};
    for (int i = 0; i < fruits.length; i++) {
      System.out.println("Fruit " + (i + 1) + ": " + fruits[i]);
    }

    for (String fruit : fruits) {
      System.out.println("Enjoy this fruit: " + fruit);
    }
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    String[] fruits = {"Apple", "Banana", "Cherry"};
    for (int i = 0; i < fruits.length; i++) {
      System.out.println("Fruit " + (i + 1) + ": " + fruits[i]);
    }

    for (String fruit : fruits) {
      System.out.println("Enjoy this fruit: " + fruit);
    }
  }
}''',
        'exercise': 'Add a new item to the fruits array and print how many fruits there are using fruits.length.',
    },
    'lesson8.html': {
        'title': 'Lesson 8: Strings',
        'icon': '📝',
        'breadcrumb': 'Home > Lessons > Lesson 8',
        'intro': 'Strings store text such as words and sentences. Java treats strings as objects, so you use methods to examine and change text safely.',
        'learn': [
            'Create and join strings with concatenation.',
            'Read common String methods like length() and charAt().',
            'Compare strings with equals() instead of ==.',
            'Convert text to upper or lower case.',
        ],
        'why': 'Text is everywhere in applications, from user names to messages. Strings provide powerful tools for working with text in Java.',
        'concepts': [
            ('String', 'Text wrapped in double quotes.'),
            ('Concatenation', 'Joining text using the + operator.'),
            ('length()', 'Returns the number of characters in the text.'),
            ('charAt()', 'Gets a character at a specific position.'),
            ('equals()', 'Compares two strings for the same text.'),
        ],
        'common': [
            'Using == to compare Strings instead of .equals().',
            'Assuming String is a primitive type instead of an object.',
            'Accessing charAt() with an invalid index.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    String first = "Java";
    String second = "Basics";
    String message = first + " " + second;
    System.out.println(message);
    System.out.println("Length: " + message.length());
    System.out.println("First char: " + message.charAt(0));
    System.out.println("Same text? " + message.equals("Java Basics"));
    System.out.println("Upper case: " + message.toUpperCase());
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    String first = "Java";
    String second = "Basics";
    String message = first + " " + second;
    System.out.println(message);
    System.out.println("Length: " + message.length());
    System.out.println("First char: " + message.charAt(0));
    System.out.println("Same text? " + message.equals("Java Basics"));
    System.out.println("Upper case: " + message.toUpperCase());
  }
}''',
        'exercise': 'Change the message string and print its length, the first character, and whether it matches "Java Basics".',
    },
    'lesson9.html': {
        'title': 'Lesson 9: Classes & Objects',
        'icon': '🏗️',
        'breadcrumb': 'Home > Lessons > Lesson 9',
        'intro': 'Classes are blueprints, and objects are the things built from those blueprints. In Java, classes define data and behavior, and objects are reusable values your program works with.',
        'learn': [
            'Define classes with fields and methods.',
            'Create objects using the new keyword.',
            'Use constructors to initialize object data.',
            'Access object behavior through methods.',
        ],
        'why': 'Object-oriented programming helps organize code around real-world concepts, making larger programs easier to design and maintain.',
        'concepts': [
            ('Class', 'A blueprint that describes data and behavior.'),
            ('Object', 'An instance of a class with its own values.'),
            ('Field', 'A variable that stores data inside an object.'),
            ('Constructor', 'A special method that creates and initializes objects.'),
            ('Method', 'A function that belongs to a class or object.'),
        ],
        'common': [
            'Putting logic in static methods instead of using object behavior.',
            'Forgetting to use new when creating an object.',
            'Exposing object fields directly instead of using methods.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    Car car = new Car("Red", 2024);
    car.showInfo();
    car.honk();
  }

  static class Car {
    String color;
    int year;

    Car(String color, int year) {
      this.color = color;
      this.year = year;
    }

    void showInfo() {
      System.out.println("Car: " + color + " " + year);
    }

    void honk() {
      System.out.println("Beep beep!");
    }
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    Car car = new Car("Red", 2024);
    car.showInfo();
    car.honk();
  }

  static class Car {
    String color;
    int year;

    Car(String color, int year) {
      this.color = color;
      this.year = year;
    }

    void showInfo() {
      System.out.println("Car: " + color + " " + year);
    }

    void honk() {
      System.out.println("Beep beep!");
    }
  }
}''',
        'exercise': 'Add a new field to the Car class, such as "model" or "doors", and print it in showInfo().',
    },
    'lesson10.html': {
        'title': 'Lesson 10: Polymorphism',
        'icon': '🔄',
        'breadcrumb': 'Home > Lessons > Lesson 10',
        'intro': 'Polymorphism lets objects of different classes be treated as instances of a common superclass. It enables flexible code that works with many related object types.',
        'learn': [
            'Use a superclass type to refer to subclass objects.',
            'Override methods to change subclass behavior.',
            'See how Java decides which method to run at runtime.',
            'Understand why polymorphism is useful for extensible code.',
        ],
        'why': 'Polymorphism reduces code duplication and makes it easier to add new object types without changing the code that uses them.',
        'concepts': [
            ('Polymorphism', 'One interface, many implementations.'),
            ('Inheritance', 'A subclass shares behavior from a superclass.'),
            ('Override', 'A subclass changes how a method works.'),
            ('Superclass', 'A parent class that defines common behavior.'),
            ('Dynamic binding', 'Java chooses the correct method at runtime.'),
        ],
        'common': [
            'Declaring variables as the subclass type instead of the superclass type.',
            'Forgetting to use @Override when overriding methods.',
            'Expecting compile-time type to determine runtime behavior.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    Animal animal = new Dog();
    animal.speak();
    animal = new Cat();
    animal.speak();
    animal = new Bird();
    animal.speak();
  }

  static class Animal {
    void speak() {
      System.out.println("Animal sound");
    }
  }

  static class Dog extends Animal {
    @Override
    void speak() {
      System.out.println("Dog says woof");
    }
  }

  static class Cat extends Animal {
    @Override
    void speak() {
      System.out.println("Cat says meow");
    }
  }

  static class Bird extends Animal {
    @Override
    void speak() {
      System.out.println("Bird says tweet");
    }
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    Animal animal = new Dog();
    animal.speak();
    animal = new Cat();
    animal.speak();
    animal = new Bird();
    animal.speak();
  }

  static class Animal {
    void speak() {
      System.out.println("Animal sound");
    }
  }

  static class Dog extends Animal {
    @Override
    void speak() {
      System.out.println("Dog says woof");
    }
  }

  static class Cat extends Animal {
    @Override
    void speak() {
      System.out.println("Cat says meow");
    }
  }

  static class Bird extends Animal {
    @Override
    void speak() {
      System.out.println("Bird says tweet");
    }
  }
}''',
        'exercise': 'Add a new subclass of Animal, such as Rabbit or Fish, and override speak() with a different message.',
    },
    'lesson11.html': {
        'title': 'Lesson 11: Exception Handling',
        'icon': '🛡️',
        'breadcrumb': 'Home > Lessons > Lesson 11',
        'intro': 'Exception handling helps Java programs deal with unexpected errors without crashing. It lets you separate normal code from error handling and keep programs running safely.',
        'learn': [
            'Use try, catch, and finally to handle runtime errors.',
            'Differentiate checked and unchecked exceptions.',
            'Throw exceptions from methods when errors occur.',
            'Use custom exception messages for clearer debugging.',
        ],
        'why': 'Errors can happen when files are missing, input is wrong, or data is invalid. Handling exceptions makes programs more stable and easier to fix.',
        'concepts': [
            ('Exception', 'An object that represents an error event.'),
            ('try', 'A block of code that may cause an exception.'),
            ('catch', 'Handles the specific exception type when it occurs.'),
            ('finally', 'Runs cleanup code even if an error happened.'),
            ('throws', 'Indicates that a method may pass an exception to its caller.'),
        ],
        'common': [
            'Catching very broad exceptions and hiding useful error details.',
            'Not closing resources after an exception occurs.',
            'Using exception handling for normal control flow instead of real errors.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    try {
      int result = divide(10, 0);
      System.out.println("Result: " + result);
    } catch (ArithmeticException ex) {
      System.out.println("Cannot divide by zero.");
    } finally {
      System.out.println("Cleanup is always done.");
    }
  }

  public static int divide(int a, int b) {
    return a / b;
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    try {
      int result = divide(10, 0);
      System.out.println("Result: " + result);
    } catch (ArithmeticException ex) {
      System.out.println("Cannot divide by zero.");
    } finally {
      System.out.println("Cleanup is always done.");
    }
  }

  public static int divide(int a, int b) {
    return a / b;
  }
}''',
        'exercise': 'Change the divisor in divide() to a valid number, then run the code and compare the output with the error case.',
    },
    'lesson12.html': {
        'title': 'Lesson 12: File I/O',
        'icon': '📁',
        'breadcrumb': 'Home > Lessons > Lesson 12',
        'intro': 'File I/O lets Java read and write information from files. This is how programs save data to disk and load it later.',
        'learn': [
            'Use FileReader and FileWriter to read and write text files.',
            'Use BufferedReader for efficient line-by-line input.',
            'Handle IOException when file operations fail.',
            'Understand relative versus absolute file paths.',
        ],
        'why': 'Files are needed for configuration, saving progress, and logging. File I/O is a key skill for real applications.',
        'concepts': [
            ('FileReader', 'Reads characters from a text file.'),
            ('FileWriter', 'Writes characters to a text file.'),
            ('BufferedReader', 'Reads text efficiently, line by line.'),
            ('IOException', 'An exception thrown for file and stream errors.'),
            ('Path', 'The location of a file on disk.'),
        ],
        'common': [
            'Using the wrong file path and getting a file not found error.',
            'Forgetting to close file streams after use.',
            'Assuming file I/O always works and not checking for exceptions.',
        ],
        'example': '''import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
  public static void main(String[] args) {
    try {
      writeFile("example.txt", "Hello Java!\nWelcome to file I/O.");
      readFile("example.txt");
    } catch (IOException e) {
      System.out.println("File error: " + e.getMessage());
    }
  }

  public static void writeFile(String fileName, String content) throws IOException {
    FileWriter writer = new FileWriter(fileName);
    writer.write(content);
    writer.close();
  }

  public static void readFile(String fileName) throws IOException {
    BufferedReader reader = new BufferedReader(new FileReader(fileName));
    String line;
    while ((line = reader.readLine()) != null) {
      System.out.println(line);
    }
    reader.close();
  }
}''',
        'textarea_code': '''import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
  public static void main(String[] args) {
    try {
      writeFile("example.txt", "Hello Java!\nWelcome to file I/O.");
      readFile("example.txt");
    } catch (IOException e) {
      System.out.println("File error: " + e.getMessage());
    }
  }

  public static void writeFile(String fileName, String content) throws IOException {
    FileWriter writer = new FileWriter(fileName);
    writer.write(content);
    writer.close();
  }

  public static void readFile(String fileName) throws IOException {
    BufferedReader reader = new BufferedReader(new FileReader(fileName));
    String line;
    while ((line = reader.readLine()) != null) {
      System.out.println(line);
    }
    reader.close();
  }
}''',
        'exercise': 'Update the file name and message text, then run the program to see the file contents printed back. Try writing multiple lines.',
    },
    'lesson13.html': {
        'title': 'Lesson 13: Collections',
        'icon': '🧠',
        'breadcrumb': 'Home > Lessons > Lesson 13',
        'intro': 'Collections are Java objects that hold groups of values. They are more powerful and flexible than arrays, supporting dynamic growth and fast lookup.',
        'learn': [
            'Use ArrayList, HashMap, and HashSet for different collection needs.',
            'Choose the right collection type based on order, uniqueness, and lookup speed.',
            'Iterate through collections using for-each loops.',
            'Understand generic types for collection values.',
        ],
        'why': 'Collections are used in most Java programs to store and manage data. They are a core part of building real-world applications.',
        'concepts': [
            ('ArrayList', 'A resizable list that keeps insertion order.'),
            ('HashMap', 'A key/value store for fast lookup.'),
            ('HashSet', 'A collection of unique values.'),
            ('Generics', 'Specifies the type stored in a collection.'),
            ('Iteration', 'Going through collection elements one by one.'),
        ],
        'common': [
            'Using a list when you need unique items and should use a Set instead.',
            'Assuming HashMap preserves insertion order; it does not.',
            'Not specifying generic types and getting warnings or errors.',
        ],
        'example': '''import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
  public static void main(String[] args) {
    ArrayList<String> names = new ArrayList<>();
    names.add("Alice");
    names.add("Bob");
    names.add("Charlie");

    HashMap<String, Integer> scores = new HashMap<>();
    scores.put("Alice", 90);
    scores.put("Bob", 85);

    HashSet<String> uniqueColors = new HashSet<>();
    uniqueColors.add("Red");
    uniqueColors.add("Blue");
    uniqueColors.add("Red");

    for (String name : names) {
      System.out.println(name + ": " + scores.get(name));
    }

    System.out.println("Unique colors: " + uniqueColors);
  }
}''',
        'textarea_code': '''import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
  public static void main(String[] args) {
    ArrayList<String> names = new ArrayList<>();
    names.add("Alice");
    names.add("Bob");
    names.add("Charlie");

    HashMap<String, Integer> scores = new HashMap<>();
    scores.put("Alice", 90);
    scores.put("Bob", 85);

    HashSet<String> uniqueColors = new HashSet<>();
    uniqueColors.add("Red");
    uniqueColors.add("Blue");
    uniqueColors.add("Red");

    for (String name : names) {
      System.out.println(name + ": " + scores.get(name));
    }

    System.out.println("Unique colors: " + uniqueColors);
  }
}''',
        'exercise': 'Add another name and score to the ArrayList and HashMap, then print the new values.',
    },
    'lesson14.html': {
        'title': 'Lesson 14: Recursion',
        'icon': '↪️',
        'breadcrumb': 'Home > Lessons > Lesson 14',
        'intro': 'Recursion is a technique where a method calls itself. It is useful for problems like factorials, tree traversal, and breaking large problems into smaller pieces.',
        'learn': [
            'Write recursive methods with a base case and a recursive step.',
            'Understand how the call stack stores each recursive call.',
            'Use recursion carefully to avoid infinite loops.',
            'See problems that recursion solves more naturally than loops.',
        ],
        'why': 'Some problems are easier to express recursively than with loops. Recursion is a core concept in algorithms and data structures.',
        'concepts': [
            ('Recursive call', 'A method calling itself.'),
            ('Base case', 'The condition that stops recursion.'),
            ('Call stack', 'Where Java remembers each method call.'),
            ('Infinite recursion', 'When the base case never occurs.'),
            ('Divide and conquer', 'Solving a large problem by solving smaller ones.'),
        ],
        'common': [
            'Missing or incorrect base cases that cause infinite recursion.',
            'Using recursion where a simple loop is clearer.',
            'Not realizing that recursion can use more memory than loops.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    System.out.println("Factorial of 5: " + factorial(5));
    System.out.println("Fibonacci of 6: " + fibonacci(6));
  }

  public static int factorial(int n) {
    if (n <= 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }

  public static int fibonacci(int n) {
    if (n <= 1) {
      return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    System.out.println("Factorial of 5: " + factorial(5));
    System.out.println("Fibonacci of 6: " + fibonacci(6));
  }

  public static int factorial(int n) {
    if (n <= 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }

  public static int fibonacci(int n) {
    if (n <= 1) {
      return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}''',
        'exercise': 'Increase the input to factorial or fibonacci and run the code. Then add a recursive method for counting down from a number to zero.',
    },
    'lesson15.html': {
        'title': 'Lesson 15: Debugging & Testing',
        'icon': '🧪',
        'breadcrumb': 'Home > Lessons > Lesson 15',
        'intro': 'Debugging and testing help you find and fix problems before your program is used. They are essential skills for writing reliable Java code.',
        'learn': [
            'Use print statements to inspect variables and program flow.',
            'Check output against expected results.',
            'Use simple assertions or test cases.',
            'Find and fix bugs by reading error messages carefully.',
        ],
        'why': 'All developers make mistakes. Debugging and testing turn those mistakes into learning opportunities and make your code dependable.',
        'concepts': [
            ('Debugging', 'Finding and fixing errors in code.'),
            ('Testing', 'Verifying the code works as expected.'),
            ('Assertion', 'A check that confirms a condition is true.'),
            ('Error messages', 'Clues from Java when something goes wrong.'),
            ('Edge case', 'A special input that can break your code if not handled.'),
        ],
        'common': [
            'Ignoring error messages instead of reading them carefully.',
            'Not testing unusual or boundary values.',
            'Fixing symptoms instead of the root cause of a bug.',
        ],
        'example': '''public class Main {
  public static void main(String[] args) {
    int result = add(3, 4);
    System.out.println("Result: " + result);
    System.out.println("Expected: 7");
    System.out.println("Pass: " + (result == 7));
  }

  public static int add(int a, int b) {
    return a + b;
  }
}''',
        'textarea_code': '''public class Main {
  public static void main(String[] args) {
    int result = add(3, 4);
    System.out.println("Result: " + result);
    System.out.println("Expected: 7");
    System.out.println("Pass: " + (result == 7));
  }

  public static int add(int a, int b) {
    return a + b;
  }
}''',
        'exercise': 'Change the numbers passed to add() and update the expected result. Run the code and see whether the test passes.',
    },
}

for filename, data in lessons.items():
    path = Path(filename)
    if not path.exists():
        print(f'Skipping missing file: {filename}')
        continue
    text = path.read_text(encoding='utf-8')
    hero_start = text.find('<section class="lesson-hero">')
    hero_end = text.find('</section>', hero_start)
    if hero_start == -1 or hero_end == -1:
        raise ValueError(f'Hero section markers not found in {filename}')
    hero_end += len('</section>')
    hero_html = f'''<section class="lesson-hero">
  <div class="hero-content">
    <div class="icon">{data['icon']}</div>
    <div>
      <h1>{data['title']}</h1>
      <p class="breadcrumb">{data['breadcrumb']}</p>
    </div>
  </div>
</section>'''
    text = text[:hero_start] + hero_html + text[hero_end:]
    content_start = text.find('<section class="lesson-content">')
    content_end = text.find('</section>', content_start)
    if content_start == -1 or content_end == -1:
        raise ValueError(f'Lesson content markers not found in {filename}')
    content_end += len('</section>')
    learn_html = ''.join([f'        <li>{item}</li>\n' for item in data['learn']])
    concepts_html = ''.join([f'        <li><strong>{title}</strong> — {desc}</li>\n' for title, desc in data['concepts']])
    common_html = ''.join([f'        <li>{item}</li>\n' for item in data['common']])
    content_html = f'''<section class="lesson-content">
    <div class="card intro">
      <h2>{data['title']}</h2>
      <p>{data['intro']}</p>
    </div>

    <div class="card">
      <h3>What you will learn</h3>
      <ul>
{learn_html}      </ul>
    </div>

    <div class="card">
      <h3>Why this matters</h3>
      <p>{data['why']}</p>
    </div>

    <div class="card">
      <h3>Important concepts</h3>
      <ul>
{concepts_html}      </ul>
    </div>

    <div class="card">
      <h3>Common mistakes</h3>
      <ul>
{common_html}      </ul>
    </div>

    <div class="card code-section">
      <div class="code-header"><span>Example Code</span></div>
      <pre>
{data['example']}
      </pre>
    </div>

    <div class="takeaway">
      <div class="icon">💡</div>
      <div>
        <h3>Key Takeaway</h3>
        <p>{data['why']}</p>
      </div>
    </div>

    <div class="lesson-nav">
      <!-- preserve existing navigation buttons from file -->
    </div>
</section>'''
    text = text[:content_start] + content_html + text[content_end:]
    exercise_start = text.find('<div class="card exercise">')
    if exercise_start != -1:
        p_start = text.find('<p>', exercise_start)
        p_end = text.find('</p>', p_start)
        if p_start != -1 and p_end != -1:
            text = text[:p_start] + f'<p>{data["exercise"]}</p>' + text[p_end + len('</p>'):]
    textarea_start = text.find('<textarea id="code">', exercise_start)
    if textarea_start != -1:
        textarea_end = text.find('</textarea>', textarea_start)
        if textarea_end != -1:
            text = text[:textarea_start + len('<textarea id="code">')] + data['textarea_code'] + text[textarea_end:]
    path.write_text(text, encoding='utf-8')
    print(f'Updated {filename}')
