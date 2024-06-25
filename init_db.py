import sqlite3


def initialize_database():
    conn = sqlite3.connect("db/database.sqlite")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INTEGER PRIMARY KEY,
        Name TEXT,
        EnrollmentYear INTEGER,
        Major TEXT,
        Gender TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Courses (
        CourseID INTEGER PRIMARY KEY,
        CourseName TEXT,
        Credits INTEGER,
        Department TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Enrollments (
        EnrollmentID INTEGER PRIMARY KEY,
        StudentID INTEGER,
        CourseID INTEGER,
        FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
        FOREIGN KEY(CourseID) REFERENCES Courses(CourseID)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Advisors (
        AdvisorID INTEGER PRIMARY KEY,
        Name TEXT,
        Department TEXT
    )
    """
    )

    conn.commit()
    conn.close()
    print("Database created and tables initialized.")


if __name__ == "__main__":
    initialize_database()
