class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_score(self):
        count = 0
        total = 0
        for grade in self.grades.values():
            total += (sum(grade) / len(grade))
            count += 1
        if count > 0:
            average_grade = round(total / count, 2)
            return average_grade
        else:
            return

    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашнее задание: {self.average_score()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} не Лектор')
            return
        return self.average_score() < other.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.courses_attached = []
        self.grades = {}

    def teacher_assessment(self, lecturer, course, grade, student):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        count = 0
        total = 0
        for grade in self.grades.values():
            total += (sum(grade) / len(grade))
            count += 1
        if count > 0:
            average_grade = round(total / count, 2)
            return average_grade
        else:
            return

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} не студент')
            return
        return self.average_score() < other.average_score()


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
best_student.courses_in_progress += ['Git']

best_student1 = Student('Ruoy1', 'Eman1', 'your_gender1')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Git']

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

cool_mentor1 = Reviewer('Some1', 'Buddy1')
cool_mentor1.courses_attached += ['Python']
cool_mentor1.courses_attached += ['Git']

cool_mentor2 = Reviewer('Some1', 'Buddy1')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Git']

cool_lecturer = Lecturer('Harry', 'Owen')
cool_lecturer.courses_attached += ['Python']

cool_lecturer1 = Lecturer('Harry1', 'Owen1')
cool_lecturer1.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 4)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 7)
cool_mentor.rate_hw(best_student1, 'Git', 7)
cool_mentor.rate_hw(best_student2, 'Git', 7)

cool_mentor1.rate_hw(best_student, 'Python', 7)
cool_mentor1.rate_hw(best_student1, 'Python', 10)
cool_mentor1.rate_hw(best_student2, 'Python', 9)
cool_mentor1.rate_hw(best_student, 'Git', 5)
cool_mentor1.rate_hw(best_student1, 'Git', 7)
cool_mentor1.rate_hw(best_student2, 'Git', 8)

cool_mentor2.rate_hw(best_student, 'Python', 10)
cool_mentor2.rate_hw(best_student1, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Python', 3)
cool_mentor2.rate_hw(best_student, 'Git', 9)
cool_mentor2.rate_hw(best_student1, 'Git', 7)
cool_mentor2.rate_hw(best_student2, 'Git', 1)

cool_lecturer.teacher_assessment(cool_lecturer, 'Python', 10, best_student)
cool_lecturer.teacher_assessment(cool_lecturer, 'Python', 7, best_student1)
cool_lecturer.teacher_assessment(cool_lecturer, 'Python', 7, best_student2)

cool_lecturer1.teacher_assessment(cool_lecturer1, 'Git', 10, best_student)
cool_lecturer1.teacher_assessment(cool_lecturer1, 'Git', 5, best_student1)
cool_lecturer1.teacher_assessment(cool_lecturer1, 'Git', 8, best_student2)

print(best_student.grades)
print(best_student1.grades)
print(best_student2.grades)
print('-----')
print(cool_lecturer.grades)
print(cool_lecturer1.grades)
print('-----')
print(cool_lecturer.average_score())
print(cool_lecturer1.average_score())
print('-----')
print(best_student.average_score())
print(best_student1.average_score())
print(best_student2.average_score())
print('-----')
print(cool_lecturer)
print(cool_mentor)
print(best_student)
print('-----')
print(cool_lecturer < best_student)

students = (best_student, best_student1, best_student2)


def average_score_students(students, course):
    count = 0
    for i in students:
        for a, b in i.grades.items():
            if a == course:
                sr = (sum(b) / len(b))
                count += sr
    print(count / len(students))


average_score_students(students, 'Python')
average_score_students(students, 'Git')

lecturer = (cool_lecturer, cool_lecturer1)


def average_score_lecturer(lecturer, course):
    count = 0
    for i in lecturer:
        for a, b in i.grades.items():
            if a == course:
                sr = (sum(b) / len(b))
                count += sr
    print(count / len(lecturer))


average_score_lecturer(lecturer, 'Python')
average_score_lecturer(lecturer, 'Git')
