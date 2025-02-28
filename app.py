"""
1) Create PostgreSQL file & schema
2) Load student data into it
3) Create Flask app/methods to get info on the table's instances
"""

from flask import Flask
from student_data import students

app = Flask('app')
app.config['students_list'] = students

# path : http://127.0.0.1:8000/students
@app.route("/students")
def print():
    # print(students)
    return students

# returns an array of students older than 20
@app.route("/students/old_students")
def old_students():
    old_students = list(filter(lambda x : x['age'] > 20, students))
    return old_students

# returns an array of students younger than 21
@app.route("/students/young_students")
def young_students():
    young_students = list(filter(lambda x : x['age'] < 21, students))
    return young_students

# returns an array of students younger than 21 and grade of A
@app.route("/students/advanced_students")
def advance_students():
    advanced_students = list(filter(lambda x : x['age'] < 21 and x['grade'] == 'A', students))
    return advanced_students

# returns an array of student objects holding the keys of 'first_name' and "last_name' and their values
@app.route("/students/condensedinfo")
def condensed_info_students():
    # This is looping through the students list of dicts & creating a new dict using each loop iteration's needed key's
    condensed_students = [{'first_name': stu['first_name'], 'last_name': stu['last_name']} for stu in students]
    return condensed_students

# returns an array containing student full name + age
@app.route("/students/studentagename")
def student_info_basics():
    # This is looping through the students list of dicts & creating a new dict using each loop iteration's needed key's    
    student_info = [{'student_name': stu['first_name'] + ' ' + stu['last_name'], 'age': stu['age']} for stu in students]    
    return student_info










app.run(debug=True, port=8000)