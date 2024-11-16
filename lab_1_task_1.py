class SchoolDiary:
    def __init__(self, subject, student, grade_list):
        self.subject = subject
        self.student = student
        self.grade_list = grade_list

    def grade(self, num):
        if num < 1 or num > 5:
            return "Недопустимое число! \nПожалуйста, введите число от 1 до 5."
        return self.grade_list.append(num)
    
    def final_grade(self):
        sum_grade = sum(self.grade_list)

        res = sum_grade / len(self.grade_list)
        print(f"Окончательная оценка: {res}")

    
    def printer(self):
        print(f"Ученик: {self.student}")
        print(f"Предмет: {self.subject}")
        print(f"Оценки: {self.grade_list}")


if __name__ == '__main__':
    obj = SchoolDiary("Информатика", "Иванов Иван", [4, 5, 5, 4, 5])

    obj.grade(3)

    obj.printer()
    obj.final_grade()
    
        