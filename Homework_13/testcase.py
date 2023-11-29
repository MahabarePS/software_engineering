import webbrowser

class GenerateHTML:
    """Class to generate an HTML file from an input file"""

    def __init__(self, input_file, output_file):
        """
        Initialize GenerateHTML class.

        Args:
        - input_file (str): The name of the input HTML file.
        - output_file (str): The name of the output HTML file to be generated.
        """
        self.input_file = input_file
        self.output_file = output_file

    def generate(self):
        """
        Generate an HTML file.

        Reads content from the input file and writes it into the output file.
        """
        with open(self.input_file, 'r') as f:
            html_syntax = f.read()
        
        with open(self.output_file, 'w') as f:
            f.write(html_syntax)

def get_user_input(prompt):
    """
    Function to get user input.

    Args:
    - prompt (str): The prompt message to display to the user.

    Returns:
    - str: User input obtained from the prompt.
    """
    return input(prompt)

def main():
    """
    Main function to execute HTML file generation.

    Prompts the user to enter input and output file names,
    generates an HTML file based on the provided input file,
    and opens the generated HTML file in the default web browser.
    """
    input_file = get_user_input('Enter <inputfile>.html: ')
    output_file = get_user_input('Enter <outputfile>.html: ')

    generator = GenerateHTML(input_file, output_file)
    generator.generate()
    
    webbrowser.open(output_file)

if __name__ == "__main__":
    main()
