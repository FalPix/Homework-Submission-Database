import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Priyanshu',
            password='MySql',
            database='homework_db'
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_table(connection):
    """Create the homework submissions table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS submissions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL,
        homework_title VARCHAR(100) NOT NULL,
        submission_date DATE,
        content TEXT
    )
    """
    cursor = connection.cursor()
    try:
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'submissions' created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def add_submission(connection, student_name, homework_title, submission_date, content):
    """Add a new homework submission."""
    add_submission_query = """
    INSERT INTO submissions (student_name, homework_title, submission_date, content)
    VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(add_submission_query, (student_name, homework_title, submission_date, content))
        connection.commit()
        print(f"Homework submission for {student_name} added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def view_submissions(connection):
    """View all homework submissions."""
    view_submissions_query = "SELECT * FROM submissions"
    cursor = connection.cursor()
    try:
        cursor.execute(view_submissions_query)
        submissions = cursor.fetchall()
        print("\n--- Current Submissions ---")
        for submission in submissions:
            print(submission)
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        create_table(connection)
        add_submission(connection, 'Nilay Shukla', 'Math Homework', '2024-12-15', 'This is my math homework.')
        add_submission(connection, 'Divyansh Gupta', 'Science Homework', '2024-12-15', 'This is my science homework.')
        view_submissions(connection)
        connection.close()

In GitHub codespace, run it anytime with:
python3 /workspaces/Homework-Submission-Database/homework.py
