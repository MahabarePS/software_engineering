from flask import Flask, render_template, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def signup():
    return render_template('signup.js')

@app.route('/validate', methods=['POST'])
def validate():
    name = request.form['name']
    password = request.form['password']

    # AC0: System must validate the strength of password
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return render_template('signup.html', error_message="Password must be at least 8 characters long and contain both letters and numbers.", name=name)

    # AC2: System must allow only alphabets to be entered in the name field and alphanumeric in the password field
    if not name.isalpha():
        return render_template('signup.html', error_message="Name field must contain only alphabets.", name=name)
    if not password.isalnum():
        return render_template('signup.html', error_message="Password field must contain only alphabets and numbers.", name=name)

    return "Signup successful!"

if __name__ == '__main__':
    app.run(debug=True)
