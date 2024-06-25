from modules.crud_operations import (
    add_student,
    update_student,
    delete_student,
    query_students,
)
from modules.analysis import analyze_data  # type: ignore


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
