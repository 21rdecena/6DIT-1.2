import sqlite3
import time

conn = sqlite3.connect('studentsv1.db')
cursor = conn.cursor()

'''
Improvement lists:

Improve add_student() function and add errors when asking for house of the new student.
Find repetitive coding pattern and turn them into functions
Improve readability (add colors, more time.sleep fucntions)


'''


def user_student_id():
    while True:
            try:
                time.sleep(.5)
                student_id = int(input("Please enter the ID of the student whose emergency info you would like to view.\n> "))
            except ValueError:
                time.sleep(.15)
                print("Invalid input! Please enter an integer!")
                continue
            break
    return student_id

def view_students():
    print("Displaying list of students...")
    print('')
    cursor.execute('SELECT id, name FROM students;')
    results = cursor.fetchall()
    for row in results:                         # for loop run for how many row of student there are
        time.sleep(0.10)
        print('Student ID:\tStudent Name:')
        print(f'{row[0]}\t\t{row[1]}\n')

def view_student_info():
    student_id = user_student_id()
    cursor.execute(f'SELECT students.name, year_born, year_level, house, extracurriculars.name, status" \
    "FROM students JOIN extracurriculars ON students.extracurricular_id = extracurriculars.id WHERE students.id = {student_id};')
    results = cursor.fetchall()
    if results:                                 # the ifs check if there was data found in the results
        for row in results:
            print()
            time.sleep(.5)
            print(f"Student Name: {row[0]}")
            print()
            time.sleep(.5)
            print(f'Year {row[2]}')
            time.sleep(.5)
            print(f'Year Born: {row[1]}')
            time.sleep(.5)
            print(f'House: {row[3]}')
            time.sleep(.5)
            print(f'Extracurricular taken: {row[4]}')
            time.sleep(.5)
            print(f'Status: {row[5]}')
    elif not results:                                       # if there was no data returned for user's query
        print()
        print("No results were found for that query.")      # prints out no data was found for query, 
        time.sleep(.75)                                     # will no longer have to account for the total number of students in the sql database
        print("Returning back to menu...")
        time.sleep(.5)

def view_student_emergency():
    student_id = user_student_id()
    cursor.execute(f'SELECT students.name, emergency_contact_name, relationship, phone_number FROM students JOIN students_emergency_info ON students.id = students_emergency_info.id WHERE students.id ={student_id};')
    results = cursor.fetchall()
    if results:                         # the ifs check if there was data found in the results
        for row in results:
            print()
            time.sleep(.5)
            print(f"{row[0]}'s Emergency Information")
            print()
            time.sleep(.5)
            print(f"{row[0]}'s Contact Name:")
            time.sleep(.25)
            print(f'{row[1]}')
            print()
            time.sleep(.5)
            print("Contact's relation with student:")
            time.sleep(.25)
            print(f'{row[2]}')
            print()
            time.sleep(.5) 
            print(f"{row[2]}'s phone number:")
            time.sleep(.25)
            print(f'{row[3]}')
    elif not results:                                # if there was no data returned for user's query
        print("No data was found for that query.")   # prints out no data was found for query, no longer have to account for the total number of students

def sort_by_criteria():
    print()
    criteria = ['1. Name', '2. Year Born', '3. Year Level', '4. House', '5. Extracurricular', '6. Status']
    x = 0
    for i in criteria:
        time.sleep(.25)
        print(f'{criteria[x]}')
        x = x + 1
    while True:
        try:
            print()
            user_criteria = int(input("By which criteria would you like to sort the student by?\n> "))
        except ValueError:
            print("Invalid input! Please enter an integer!")
            continue
        if user_criteria > 6 or user_criteria <= 0:
            print("Please choose a number between 1-6!")
            continue
        break
    if user_criteria == 1:
        cursor.execute(f'SELECT name FROM students ORDER BY name;')
        results = cursor.fetchall()
        print("Printing the students' name alphabetically by the first letter of their name...")
        print()
        for row in results:
            time.sleep(.15)
            print(row[0])
    if user_criteria == 2:
        cursor.execute(f'SELECT name, year_born FROM students ORDER BY year_born')
        results = cursor.fetchall()
        print("Printing the students' in order of the year they were born... ")
        print()
        for row in results:
            time.sleep(.15)
            print(f'{row[0]}\t\t\t{row[1]}')
    if user_criteria == 3:
        cursor.execute(f'SELECT name, year_level FROM students ORDER BY year_level')
        results = cursor.fetchall()
        print("Printing the students in order of their year level...")
        print()
        for row in results:
            time.sleep(.15)
            print(f'{row[0]}\t\t\t{row[1]}')
    if user_criteria == 4:
        cursor.execute(f'SELECT name, house FROM students ORDER BY house')
        results = cursor.fetchall()
        print("Printing the students in order of their house...")
        print()
        for row in results:
            time.sleep(.15)
            print(f'{row[0]}\t\t\t{row[1]}')
    if user_criteria == 5:
        cursor.execute(f'SELECT students.name, extracurriculars.name FROM students JOIN extracurriculars ON students.extracurricular_id = extracurriculars.id ORDER BY extracurriculars.name')
        results = cursor.fetchall()
        print("Printing the students in order by the extracurricular they have taken...")
        print()
        for row in results:
            time.sleep(.15)
            print(f'{row[0]}\t\t\t{row[1]}')
    if user_criteria == 6:
        cursor.execute(f'SELECT name, status FROM students ORDER BY status')
        results = cursor.fetchall()
        print("Printing the students in order of their status...")
        print()
        for row in results:
            time.sleep(.15)
            print(f'{row[0]}\t\t\t{row[1]}')

def update_status():
    while True:
        try:
            student_id = int(input("Please enter the ID of the student whose information you would like to change.\n> "))
        except ValueError:
            time.sleep(.15)
            print("Invalid input! Please enter an integer!")
            continue
        break
    cursor.execute(f'SELECT * FROM students WHERE id={student_id};')
    check_value = cursor.fetchall()

    if not check_value:
        print("No student was found with that ID.")
    if check_value:
        status_options = ['1. Active', '2. Graduated', '3. Inactive']
        x = 0
        for i in status_options:
            time.sleep(.15)
            print(f'{status_options[x]}')
            x = x + 1
    while True:
        choices = [1,2,3]
        try:
            user_choice = int(input("Please choose what status you would like to update to the student.\n> "))
        except ValueError:
            print("Invalid input, please enter an integer!")
            continue
        if user_choice not in choices:
            print("Invalid input, please choose a option from 1-3!")
            continue
        elif user_choice == 1:
            cursor.execute(f'UPDATE students SET status=? WHERE id=?;', ("Active", student_id))
            conn.commit()
            print("Successfully updated students' status.")
            break
        elif user_choice == 2:
            cursor.execute(f'UPDATE students SET status=? WHERE id=?;', ("Graduated", student_id))
            conn.commit()
            print("Successfully updated students' status.")
            break
        elif user_choice == 3:
            cursor.execute(f'UPDATE students SET status=? WHERE id=?;', ("Inactive", student_id))
            conn.commit()
            print("Successfully updated students' status.")
            break

def add_student():
    print("Adding a student to database...")
    student_name = input("What is the students' name?\n> ").strip()
    while True:
        try:
            student_born = int(input("What year was the student born?\n> "))
            break
        except ValueError:
            print("Invalid input, please enter an integer!")
            continue
    student_year_level_options = [9,10,11,12,13]
    while True:
        try:
            student_year_level = int(input("What year level will the student be taking?\n> "))
        except ValueError:
            print("Invalid input, please enter an integer!")
            continue
        if student_year_level not in student_year_level_options:
            print("Invalid input, please choose between years 9-13.")
            continue
        break   
    student_house = input("What house will the student be in? (Arthur, Duncan, Fox, Mackenzie, Hay)\n> ")
    extracurriculars = ['1. Student Council', '2. Debating Club', '3. Musical', '4. Chess Club', '5. Basketball', '6. Peer Mentoring', '7. Jazz Band', '8. Science Buskers Academy', '9. Badminton', '10. Volleyball']
    extracurricular_options = [1,2,3,4,5,6,7,8,9,10]
    x = 0
    for i in extracurriculars:
        time.sleep(.15)
        print(f'{extracurriculars[x]}')
        x = x + 1
    while True:
        try:
            student_extracurricular = int(input("What extracurricular will the student be taking part in?\n> ")) 
        except ValueError:
            print("Invalid input, please enter an integer!")
            continue
        if student_extracurricular not in extracurricular_options:
            print("Invalid input, please enter a number between 1-10!")
            continue
        break
    cursor.execute('INSERT INTO students (name, year_born, year_level, house, extracurricular_id, status) VALUES (?, ?, ?, ?, ?, ?)', (student_name, student_born, student_year_level, student_house, student_extracurricular, "Active"))
    conn.commit()
    print("Student has been successfully added.")

def database_menu():
    menu_options = ["1. View list of students", "2. View a students' information", "3. View a students' emergency information",'4. Sort by criteria',
                    '5. Update the status of a student','6. Add a student to the database', '7. Exit program']
    x = 0
    print('')
    print('Students Database Menu:')
    print('')
    for i in menu_options:
        time.sleep(.25)
        print(f'{menu_options[x]}')
        x = x + 1
    
                
data_options = [1,2,3,4,5,6,7]
print('Welcome to the Students Database!')
print('What would you like to do?')



while True:
    database_menu()
    try:
        user_choice = int(input("> "))
    except ValueError:
        print("Invalid input, please enter an integer!")
        continue
    if user_choice not in data_options:
        print("Invalid input, please enter a number between 1-7!")
        continue
    elif user_choice == 1:
        view_students()
        continue
    elif user_choice == 2:
        print()
        view_student_info()
        continue
    elif user_choice == 3:
        view_student_emergency()
        continue
    elif user_choice == 4:
        sort_by_criteria()
        continue
    elif user_choice == 5:
        update_status()
        continue
    elif user_choice == 6:
        add_student()
        continue
    elif user_choice == 7:
        print("Exiting program...")
        time.sleep(2)
        break    

conn.close()