# Student Information Management System

This project is a simple student information management system using Python and SQLite. It allows you to perform CRUD (Create, Read, Update, Delete) operations on student records and perform data analysis on the stored information.

## Project Structure

    student-info-system/
    │
    ├── db/
    │ └── database.sqlite
    │
    ├── modules/
    │ ├── database.py
    │ ├── analysis.py
    │ ├── crud_operations.py
    │
    ├── main.py
    ├── init_db.py
    └── requirements.txt

## Requirements

- Python 3.x
- `pandas` library

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/student-info-system.git
cd student-info-system


2. Create and Activate a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

python -m venv env

# On Windows
env\Scripts\activate

# On MacOS/Linux
source env/bin/activate

3. Update pip to the Latest Version
python -m pip install --upgrade pip


4. Install the Required Packages
Create a requirements.txt file with the following content:
pandas


Then install the dependencies:
pip install -r requirements.txt


5. Create the db Directory
mkdir db


6. Initialize the Database
Run the init_db.py script to create the database and initialize the tables:
python init_db.py


You should see the following message:
Database created and tables initialized.


7. Run the Main Script
Run the main.py script to perform example CRUD operations and data analysis:
python main.py


You should see the output of the CRUD operations and the analysis, similar to the following:
(1, 'Alice', 2020, 'Data Science', 'F')
Student Count by Major:
Data Science    1
Name: Major, dtype: int64

Gender Ratio by Major:
Gender         F
Major
Data Science  1.0


Modules
1. modules/database.py
This module contains the function to get a connection to the SQLite database.

import sqlite3

def get_connection():
    return sqlite3.connect('db/database.sqlite')


2. modules/crud_operations.py
This module contains functions to perform CRUD operations on the student records.

add_student(student_id, name, enrollment_year, major, gender)
update_student(student_id, name=None, enrollment_year=None, major=None, gender=None)
delete_student(student_id)
query_students()

3. modules/analysis.py
This module contains the function to perform data analysis on the student records.

analyze_data()




Example Operations
In the main.py script, the following operations are performed:

Adding students to the database.
Updating a student's information.
Deleting a student from the database.
Querying and printing all students.
Analyzing and printing student count by major and gender ratio by major.


from modules.crud_operations import (
    add_student,
    update_student,
    delete_student,
    query_students,
)
from modules.analysis import analyze_data

def main():
    # Example operations
    add_student(1, "Alice", 2020, "Computer Science", "F")
    add_student(2, "Bob", 2021, "Mathematics", "M")
    update_student(1, major="Data Science")
    delete_student(2)

    students = query_students()
    for student in students:
        print(student)

    student_count, gender_ratio = analyze_data()
    print("Student Count by Major:")
    print(student_count)
    print("\nGender Ratio by Major:")
    print(gender_ratio)

if __name__ == "__main__":
    main()


```

License
This project is licensed under the MIT License. See the LICENSE file for more information.

This `README.md` file provides comprehensive instructions for setting up and running the Student Information Management System, as well as a brief overview of the project's structure and functionality.
