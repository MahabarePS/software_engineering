"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Final Exam Code
Submited by: Prasad Sadanand Mahabare
"""
import sqlite3
import json
from typing import List, Tuple

class DatabaseManager:
    _instance = None

    def __new__(cls):
        # Singleton implementation: Ensures only one instance of DatabaseManager is created
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Connect to the SQLite database
            cls._instance.conn = sqlite3.connect('courses.db')
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def create_table(self):
        # Creates a table named 'courses' if it doesn't exist in the database
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                semester TEXT,
                course TEXT,
                instructor TEXT,
                location TEXT
            )
        ''')
        self.conn.commit()

    def save_to_database(self, data: List[Tuple[str, str, str, str]]):
        # Inserts data into the 'courses' table in the database
        self.cursor.executemany('''
            INSERT INTO courses (semester, course, instructor, location)
            VALUES (?, ?, ?, ?)
        ''', data)
        self.conn.commit()

    def get_data_from_database(self):
        # Retrieves all data from the 'courses' table in the database
        self.cursor.execute('SELECT * FROM courses')
        return self.cursor.fetchall()

    def read_json(self, filename: str) -> List[Tuple[str, str, str, str]]:
        # Reads data from a JSON file and converts it into a list of tuples
        with open(filename, 'r') as file:
            data = json.load(file)
            courses_data = [
                (course['semester'], course['course'], course['instructor'], course['location'])
                for course in data
            ]
            return courses_data

    # def create_html_table(self, data: List[Tuple[str, str, str, str]]) -> str:
    #     # Creates an HTML table from a list of tuples containing course information
    #     table_content = '<table border="1"><tr><th>Semester</th><th>Course</th><th>Instructor</th><th>Location</th></tr>'
    #     for row in data:
    #         table_content += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>'
    #     table_content += '</table>'
    #     return table_content
    def create_html_table(self, data: List[Tuple[str, str, str, str]]) -> str:
    # Creates an HTML table from a list of tuples containing course information
        table_content = '<table border="1">\n'
        table_content += '<tr><th>Semester</th><th>Course</th><th>Instructor</th><th>Location</th></tr>\n'
    
        for row in data:
            table_content += '<tr>'
            for item in row:
                table_content += f'<td>{item}</td>'
            table_content += '</tr>\n'
    
        table_content += '</table>'
        return table_content


    def main(self):
        # The main function that orchestrates the entire process
        self.create_table()  # Create 'courses' table in the database
        courses_data = self.read_json('courses.json')  # Read data from JSON file
        self.save_to_database(courses_data)  # Save data to the database
        data_from_db = self.get_data_from_database()  # Retrieve data from the database
        html_table = self.create_html_table(data_from_db)  # Create HTML table
        # Write HTML table content to a file named 'courses.html'
        with open('courses.html', 'w') as html_file:
            html_file.write(html_table)


if __name__ == "__main__":
    # Entry point of the script: Create an instance of DatabaseManager and execute the main function
    db_manager = DatabaseManager()
    db_manager.main()
