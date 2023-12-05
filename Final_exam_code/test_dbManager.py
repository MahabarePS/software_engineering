"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Final Exam Code
Submited by: Prasad Sadanand Mahabare
"""
import unittest
import sqlite3
from unittest.mock import mock_open
from dbManager import DatabaseManager
from mock import patch

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        # Create a test database and table
        self.conn = sqlite3.connect(':memory:')  # Use an in-memory database for testing
        self.cursor = self.conn.cursor()
        self.db_manager = DatabaseManager()
        self.db_manager.conn = self.conn
        self.db_manager.cursor = self.cursor
        self.db_manager.create_table()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_save_to_database(self):
        # Test saving data to the database
        test_data = [
            ('Fall 2023', 'ACS 560', 'Matthew Parker', 'KT 246'),
            ('Fall 2023', 'CS 560', 'Jin Yoo', 'ET 116'),
        ]
        self.db_manager.save_to_database(test_data)
        self.cursor.execute('SELECT * FROM courses')
        saved_data = self.cursor.fetchall()
        self.assertEqual(saved_data, test_data)

    def test_read_json(self):
        # Test reading data from a JSON file
        test_json = '[{"semester": "Fall 2023", "course": "ACS 560", "instructor": "Matthew Parker", "location": "KT 246"}]'
        with patch('builtins.open', mock_open(read_data=test_json)):
            data = self.db_manager.read_json('test.json')
        expected_data = [('Fall 2023', 'ACS 560', 'Matthew Parker', 'KT 246')]
        self.assertEqual(data, expected_data)

    def test_create_html_table(self):
        # Test creating HTML table from data
        test_data = [
            ('Fall 2023', 'ACS 560', 'Matthew Parker', 'KT 246'),
            ('Spring 2024', 'ACS 545', 'Zesheng Chen', 'ET 112'),
        ]
        expected_html = '<table border="1">\n<tr><th>Semester</th><th>Course</th><th>Instructor</th><th>Location</th></tr>\n<tr><td>Fall 2023</td><td>ACS 560</td><td>Matthew Parker</td><td>KT 246</td></tr>\n<tr><td>Spring 2024</td><td>ACS 545</td><td>Zesheng Chen</td><td>ET 112</td></tr>\n</table>'
        html_table = self.db_manager.create_html_table(test_data)
        self.assertEqual(html_table, expected_html)

if __name__ == '__main__':
    unittest.main()
