"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Homework_03
Goal: Learn Dry principles
Submited by: Prasad Sadanand Mahabare
"""
import webbrowser # To view the newly created HTML in web browser

# Generate file
file = open('hw3.html','w')

# Html file that needs HTML syntax
with open('sample.html','r') as f:
    html_syntax = f.read()

# Write the syntax in blank html
file.write(html_syntax)

# Close the file
file.close()

#Open the generated HTML file
webbrowser.open('hw3.html')