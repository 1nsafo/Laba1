groupmates = [
    {
        "name": "Руслае",
        "surname": "Соколенко",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 3, 4]
    },
    {
        "name": "Руслан",
        "surname": "Макоев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Евгений",
        "surname": "Рохман",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 2, 5]
    },
    {
        "name": "Никита",
        "surname": "Чернышов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Момотенко",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 4, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        marks_list = student['marks']
        result = (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))
need = int(input())

print_students(groupmates)
