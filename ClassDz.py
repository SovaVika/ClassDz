class Student:

    def __init__(self, name, age, course, aver_mark):
        self.name = name
        self.age = age
        self.course = course
        self.aver_mark = aver_mark

    def get_info (self):
        print("Ім'я -", self.name)
        print("Вік -", self.age)
        print("Курс -", self.course)
        print("Середній бал -", self.aver_mark)

    def increase_year (self):
        self.course += 1
        print(self.name, "перейшов(ла) на", self.course, "курс")

    def update_grade (self, new_grade):
        self.aver_mark = (self.aver_mark + new_grade) / 2
        print(self.name, "написав(ла) іспит на", new_grade, "бал(ів, а), тепер його(ЇЇ) середній бал -", round(self.aver_mark))
        print("")

student1 = Student("Саша", 17,1,86)
student2 = Student("Олег", 19,3,56)
student3 = Student("Аня", 18,2,98)

student1.get_info()
student1.increase_year()
student1.update_grade(72)

student2.get_info()
student2.increase_year()
student2.update_grade(43)

student3.get_info()
student3.increase_year()
student3.update_grade(97)