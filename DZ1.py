def averageRating(grades):
    grade = list(grades.values())
    rez = 0
    for elementList in grade:
        rez += sum(elementList)/len(elementList)
    return rez / len(grade)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rating = averageRating(self.grades)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {rating}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        rating = averageRating(self.grades)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {rating}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C']
best_student.finished_courses += ['HTML']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['C']
cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(best_student, 'Python', 4)
cool_Reviewer.rate_hw(best_student, 'C', 4)
cool_Reviewer.rate_hw(best_student, 'C', 5)
 
cool_Lecturer = Lecturer('Lecturer', 'Buddy')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['C']

best_student.rate_hw(cool_Lecturer, 'Python', 8)
best_student.rate_hw(cool_Lecturer, 'Python', 10)
best_student.rate_hw(cool_Lecturer, 'C', 7)
best_student.rate_hw(cool_Lecturer, 'C', 10)

print(cool_Reviewer)
print(cool_Lecturer)
print(best_student)