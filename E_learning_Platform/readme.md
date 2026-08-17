# E-Learning Platform Using OOP and Inheritance

## 📌 Project Overview

This project is a basic **E-Learning Platform** developed using **Python Object-Oriented Programming (OOP)**.

The application demonstrates how different users interact with courses on an online learning platform. It uses **inheritance** to create specialized user types such as students and instructors.

The system allows:

* Students to enroll in courses
* Students to view their enrolled courses
* Students to update and check course progress
* Instructors to add courses
* Instructors to view the courses they teach
* Courses to store information such as name, duration, details, and instructor

---

## 🧠 OOP Concepts Used

### 1. Classes and Objects

The project uses the following classes:

* `User`
* `Student`
* `Instructor`
* `Course`

Objects are created from these classes to represent real-world users and courses.

---

### 2. Inheritance

The `User` class acts as the parent class.

```text
User
│
├── Student
│
└── Instructor
```

Both `Student` and `Instructor` inherit the common attributes:

* Name
* Email
* User ID

```python
class Student(User):
```

```python
class Instructor(User):
```

This avoids repeating the same code in both child classes.

---

### 3. Encapsulation

Each class groups related data and functionality together.

For example, the `Student` class stores:

```text
enrolled_courses
course_progress
```

It also contains methods to manage student-related operations.

---

## 🏗️ Classes and Responsibilities

### `User`

The `User` class is the parent class containing common user information.

#### Attributes

* `name`
* `email`
* `user_id`

```python
class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
```

---

### `Student`

The `Student` class inherits from `User`.

```python
class Student(User):
```

#### Additional Attributes

* `enrolled_courses` – Stores the courses enrolled by the student
* `course_progress` – Stores the progress of each enrolled course

#### Methods

| Method                                   | Description                     |
| ---------------------------------------- | ------------------------------- |
| `enrolled_course(course)`                | Enrolls the student in a course |
| `view_enrolled_courses()`                | Displays all enrolled courses   |
| `update_progress(course_name, progress)` | Updates progress for a course   |
| `check_progress()`                       | Displays course progress        |

---

### `Instructor`

The `Instructor` class also inherits from `User`.

```python
class Instructor(User):
```

#### Additional Attribute

* `course_data` – Stores the courses created or taught by the instructor

#### Methods

| Method               | Description                                   |
| -------------------- | --------------------------------------------- |
| `add_course(course)` | Adds a course to the instructor's course list |
| `display_course()`   | Displays all courses taught by the instructor |

When an instructor adds a course, the instructor's name is assigned to that course.

```python
course.instructor = self.name
```

---

### `Course`

The `Course` class represents an individual course.

#### Attributes

* `course_name`
* `months`
* `details`
* `instructor`

#### Method

| Method             | Description                         |
| ------------------ | ----------------------------------- |
| `display_course()` | Returns the complete course details |

---

## 👥 Users Created

### Students

| Student ID | Name   | Email                             |
| ---------- | ------ | --------------------------------- |
| S1         | Yamuna | [y@gmail.com](mailto:y@gmail.com) |
| S2         | Riya   | [r@gmail.com](mailto:r@gmail.com) |

### Instructors

| Instructor ID | Name  | Email                                     |
| ------------- | ----- | ----------------------------------------- |
| I1            | Shasi | [s@gmail.com](mailto:s@gmail.com)         |
| I2            | Ishan | [ishan@gmail.com](mailto:ishan@gmail.com) |

---

## 📚 Courses Created

| Course        | Duration | Details                           |
| ------------- | -------: | --------------------------------- |
| Python        | 2 Months | Python fundamentals for beginners |
| System Design | 3 Months | System Design                     |
| AI Agents     | 2 Months | Multilevel Agents                 |

---

## 🔄 Program Workflow

### Step 1: Create Users

Two students and two instructors are created.

```python
student1 = Student("Yamuna", "y@gmail.com", "s1")
student2 = Student("Riya", "r@gmail.com", "s2")

instructor1 = Instructor("Shasi", "s@gmail.com", "I1")
instructor2 = Instructor("Ishan", "ishan@gmail.com", "I2")
```

---

### Step 2: Create Courses

Three courses are created.

```python
course1 = Course("python", 2, "Python fundamentals for beginners")

course2 = Course("system design", 3, "System Design")

course3 = Course("ai Agents", 2, "Multilevel Agents")
```

---

### Step 3: Instructors Add Courses

Instructor Shasi teaches Python and AI Agents.

```python
instructor1.add_course(course1)
instructor1.add_course(course3)
```

Instructor Ishan teaches System Design.

```python
instructor2.add_course(course2)
```

---

### Step 4: Student Enrolls in a Course

Yamuna enrolls in the Python course.

```python
student1.enrolled_course(course1)
```

The course is added to the student's `enrolled_courses` list, and the initial progress is set to `0`.

---

### Step 5: Update Course Progress

The student's progress is updated.

```python
student1.update_progress("python", 60)
```

The progress is then displayed using:

```python
student1.check_progress()
```

---

## 📂 Project Structure

```text
E-Learning-Platform/
│
├── main.py
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone or Download the Project

Save the Python code in a file named:

```text
main.py
```

### 2. Open the Terminal

Navigate to the project directory.

### 3. Run the Program

```bash
python main.py
```

---

## 💻 Expected Functionality

The program demonstrates the following workflow:

```text
Instructor Shasi added new course python
Instructor Shasi added new course ai Agents
Instructor Ishan added new course system design

Courses taught by Shasi

Yamuna enrolled in python

Courses enrolled by Yamuna
python

Yamuna's Course progress:
python: 0

Progress updated for python

Yamuna's Course progress:
python: 60
```

---

## 🔗 Class Relationship

```text
                 User
                   │
          ┌────────┴────────┐
          │                 │
       Student          Instructor
          │                 │
          │                 ├── Add Course
          │                 └── Display Courses
          │
          ├── Enroll Course
          ├── View Courses
          ├── Update Progress
          └── Check Progress

                   │
                 Course
                   │
          ┌────────┼────────┐
          │        │        │
       Name     Duration   Details
```

---

## 🚀 Future Improvements

This project can be extended with additional features such as:

* Multiple students enrolling in multiple courses
* Course completion certificates
* Login and authentication system
* Course ratings and reviews
* Assignments and quizzes
* Automatic progress calculation
* Student and instructor dashboards
* Data storage using CSV files or databases
* Course search functionality
* Payment and subscription features

---

## 🛠️ Technologies Used

* Python
* Object-Oriented Programming
* Inheritance
* Lists
* Dictionaries
* Classes and Objects

---

## 🎯 Learning Outcome

By completing this project, you can understand:

* How to create classes and objects in Python
* How inheritance works
* How to use `super()` to initialize parent class attributes
* How objects interact with other objects
* How to store multiple objects inside lists
* How to manage data using dictionaries
* How OOP can be used to model a real-world E-Learning Platform

---

## Author

**E-Learning Platform – Python OOP Project**
