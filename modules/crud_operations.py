from modules.database import get_connection


def add_student(student_id, name, enrollment_year, major, gender):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
    INSERT INTO Students (StudentID, Name, EnrollmentYear, Major, Gender)
    VALUES (?, ?, ?, ?, ?)
    """,
        (student_id, name, enrollment_year, major, gender),
    )
    conn.commit()
    conn.close()


def update_student(
    student_id, name=None, enrollment_year=None, major=None, gender=None
):
    conn = get_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute(
            """
        UPDATE Students SET Name = ? WHERE StudentID = ?
        """,
            (name, student_id),
        )
    if enrollment_year:
        cursor.execute(
            """
        UPDATE Students SET EnrollmentYear = ? WHERE StudentID = ?
        """,
            (enrollment_year, student_id),
        )
    if major:
        cursor.execute(
            """
        UPDATE Students SET Major = ? WHERE StudentID = ?
        """,
            (major, student_id),
        )
    if gender:
        cursor.execute(
            """
        UPDATE Students SET Gender = ? WHERE StudentID = ?
        """,
            (gender, student_id),
        )
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
    DELETE FROM Students WHERE StudentID = ?
    """,
        (student_id,),
    )
    conn.commit()
    conn.close()


def query_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students
