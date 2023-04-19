import sqlite3

# подключаемся к базе данных
conn = sqlite3.connect('teatchers.db')

# создаем курсор для взаимодействия с базой данных
cursor = conn.cursor()

# создаем таблицу Students
cursor.execute('''CREATE TABLE Students
                  (Student_Id INTEGER PRIMARY KEY,
                   Student_Name TEXT,
                   School_Id INTEGER)''')

# наполняем таблицу данными
students_data = [(1, 'Иван', 201),
                 (2, 'Петр', 202),
                 (3, 'Анастасия', 203),
                 (4, 'Игорь', 204)]

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?)", students_data)

# сохраняем изменения
conn.commit()

# получаем информацию о студенте по его ID
student_id = 201
cursor.execute(
    "SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name "
    "FROM Students JOIN School ON School.School_Id =  School.School_Id WHERE Students.School_Id=?",
    (student_id,))
student_data = cursor.fetchone()

# выводим информацию
print("ID студента:", student_data[0])
print("Имя студента:", student_data[1])
print("ID школы:", student_data[2])
print("Название школы:", student_data[3])

# закрываем соединение с базой данных
conn.close()
