"""
University: Purdue University Fort Wayne
Semester: Fall 2023
Class: ACS560
Professor: Matthew Parker
Assignment: Homework_03
Goal: Learn Dry principles
Submited by: Prasad Sadanand Mahabare
"""
import webbrowser 

"""DRY Principle 1: Code with good abstraction which is easy to read and tells what a function does"""
class GenerateHTML:

  def __init__(self, input_file, output_file):
    self.input_file = input_file
    self.output_file = output_file

  def generate(self):
    # Open and read input file
    with open(self.input_file,'r') as f:
      html_syntax = f.read()

    # Open output file and write html syntax
    with open(self.output_file,'w') as f:
      f.write(html_syntax)

"""DRY Principle 2: Write unique login in one place to avoid copy+paste"""
# Get file names from user  
input_file = input('Enter <sample>.html: ')
output_file = input('Enter <hw3>.html: ')

# Create object and generate file
generator = GenerateHTML(input_file, output_file)
generator.generate()

# Open the generated file
webbrowser.open(output_file)
"""DRY Principle 3: Don't oversimplify that will add more complexity.

   For example. "hw3_No_DRY.py" is a simple and easy script but when it comes to below test case things gets teadious
   TEST CASE: duplicate 4096 different html pages

   The above code has:
   1. Object attributes than variables
   2. read/write logic in generate method
   3. Files are gathered once than multiple times
   4. One object is created than calling the class repeatedly
"""