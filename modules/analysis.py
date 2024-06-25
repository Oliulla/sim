import sqlite3
import pandas as pd  # type: ignore


def analyze_data():
    conn = sqlite3.connect("db/database.sqlite")
    df = pd.read_sql_query("SELECT * FROM Students", conn)

    gender_ratio = (
        df.groupby("Major")["Gender"].value_counts(normalize=True).unstack().fillna(0)
    )
    student_count = df["Major"].value_counts()

    conn.close()

    return student_count, gender_ratio


if __name__ == "__main__":
    student_count, gender_ratio = analyze_data()
    print("Student Count by Major:")
    print(student_count)
    print("\nGender Ratio by Major:")
    print(gender_ratio)
