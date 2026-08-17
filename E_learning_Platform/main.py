class User:
    def __init__(self,name,email,user_id):
        self.name=name
        self.email=email
        self.user_id=user_id

class Student(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses=[]
        self.course_progress={}

    def enrolled_course(self,course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            self.course_progress[course.course_name]=0
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} already enrolled in {course.course_name}")

    def view_enrolled_courses(self):
        print(f"Courses enrolled by {self.name}")
        if len(self.enrolled_courses) ==0:
            print("No courses enrolled")
        else:
            for course in self.enrolled_courses:
                print(f"{course.course_name}")

    def update_progress(self,course_name,progress):
        if course_name in self.course_progress:
            self.course_progress[course_name]=progress
            print(f"Progress updated for {course_name}")
        else:
            print("Course not found")

    def check_progress(self):
        print(f"{self.name}'s Course progress: ")
        if len(self.course_progress)==0:
            print("No courses enrolled")
        else:
            for course,progress in self.course_progress.items():
                print(f"{course}:{progress}")

class Instructor(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.course_data=[]

    def add_course(self,course):
        self.course_data.append(course)
        course.instructor= self.name
        print(f'Instructor {self.name} added new course {course.course_name}')

    def display_course(self):
        print(f"Courses taught by {self.name}")
        if len(self.course_data) ==0:
            print('No courses available')
        for course in self.course_data:
           course.display_course()

class Course:
    def __init__(self,course_name,months,details,):
        self.course_name=course_name
        self.months=months
        self.details=details

    def display_course(self):
        return f"Name: {self.course_name}\nDuration:{self.months} Months\nDetails:{self.details}\nInstructor:{self.instructor}"


# 2 students
student1= Student("Yamuna","y@gmail.com","s1")
student2=Student("Riya","r@gmail.com","s2")

# 2 instructors
instructor1=Instructor("Shasi","s@gmail.com","I1")
instructor2=Instructor("Ishan","ishan@gmail.com","I2")

# 3 courses
course1= Course("python",2,"Python fundamentals for beginners")
course2= Course("system design",3,"System Design")
course3= Course("ai Agents",2,"Multilevel Agents")

instructor1.add_course(course1)
instructor1.add_course(course3)
instructor2.add_course(course2)

instructor1.display_course()


student1.enrolled_course(course1)
student1.view_enrolled_courses()
student1.check_progress()

student1.update_progress("python",60)
student1.check_progress()



    
        
