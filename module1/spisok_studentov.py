students = ["Анна", "Борис", "Виктория", "Григорий"]

print("Список студентов:")
for index, student in enumerate(students):
    print(f"#{index} {student}")

serch_name = input("\nВвеидте имя для поиска: ")
found = False

for student in students:
    if student.lower() == serch_name.lower():
        print(f"Студент {student} найден!")
        found = True
        break

if not found:
    print("Студент не найден!")