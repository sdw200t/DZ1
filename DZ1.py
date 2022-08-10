def averageRating(grades):
    grade = list(grades.values())
    rez = 0
    for elementList in grade:
        rez += sum(elementList)/len(elementList)
    return rez / len(grade)

def averageForHomework(students, cours):
    rez = 0
    for student in students:
        grade = student.grades[cours]
        rez += sum(grade)/len(grade)
    return rez / len(students)

def averageForcours(lecturers, cours):
    rez = 0
    for lecturer in lecturers:
        grade = lecturer.grades[cours]
        rez += sum(grade)/len(grade)
    return rez / len(lecturers)

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

    def __lt__(self, other):
        return averageRating(self.grades) < averageRating(other.grades)
        
    def __le__(self, other):
        return averageRating(self.grades) <= averageRating(other.grades)

    def __eq__(self, other):
        return averageRating(self.grades) == averageRating(other.grades)

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

    def __lt__(self, other):
        return averageRating(self.grades) < averageRating(other.grades)
        
    def __le__(self, other):
        return averageRating(self.grades) <= averageRating(other.grades)

    def __eq__(self, other):
        return averageRating(self.grades) == averageRating(other.grades)

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

bad_student = Student('Bad', 'Student', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['C']
bad_student.finished_courses += ['HTML']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['C']
cool_Reviewer.rate_hw(best_student, 'Python', 7)
cool_Reviewer.rate_hw(best_student, 'Python', 4)
cool_Reviewer.rate_hw(best_student, 'C', 4)
cool_Reviewer.rate_hw(best_student, 'C', 5)
cool_Reviewer.rate_hw(bad_student, 'Python', 9)
cool_Reviewer.rate_hw(bad_student, 'Python', 4)
cool_Reviewer.rate_hw(bad_student, 'C', 4)
cool_Reviewer.rate_hw(bad_student, 'C', 5)
 
cool_Lecturer = Lecturer('Lecturer', 'Buddy')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['C']

bad_Lecturer = Lecturer('Bad', 'Lecturer')
bad_Lecturer.courses_attached += ['Python']
bad_Lecturer.courses_attached += ['C']

best_student.rate_hw(cool_Lecturer, 'Python', 8)
best_student.rate_hw(cool_Lecturer, 'Python', 10)
best_student.rate_hw(cool_Lecturer, 'C', 7)
best_student.rate_hw(cool_Lecturer, 'C', 10)
best_student.rate_hw(bad_Lecturer, 'Python', 8)
best_student.rate_hw(bad_Lecturer, 'Python', 10)
best_student.rate_hw(bad_Lecturer, 'C', 7)
best_student.rate_hw(bad_Lecturer, 'C', 10)

print(cool_Reviewer)
print()
print(cool_Lecturer)
print()
print(bad_Lecturer)
print()
print(best_student)
print()
print(bad_student)
print()
print(best_student==bad_student)
print(best_student<bad_student)
print()
print(cool_Lecturer==bad_Lecturer)
print(cool_Lecturer<bad_Lecturer)
print()
print(averageForHomework([best_student, bad_student], 'Python'))
print(averageForcours([cool_Lecturer, bad_Lecturer], 'C'))