from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
 
# Configure the SQLAlchemy database URI for your specific database system
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Winacs%40560$$@127.0.0.1:3306/user'
db = SQLAlchemy(app)
 
# Define a model for the 'signup' table
class Signup(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
 
@app.route('/')
def signup():
    return render_template('SignUpForm.js')
 
@app.route('/validate', methods=['POST'])
def validate():
    username = request.json['name']
    password = request.json['password']
 
    # AC0: System must validate the strength of the password
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return jsonify(error_message="Password must be at least 8 characters long and contain both letters and numbers")
 
    # AC2: System must allow only alphabets to be entered in the name field and alphanumeric in the password field
    if not username.isalpha():
        return jsonify(error_message="Name field must contain only alphabets")
    if not password.isalnum():
        return jsonify(error_message="Password field must contain only alphabets and numbers")
 
    # Insert user data into the 'signup' table
    new_signup = Signup(username=username, password=password)
    db.session.add(new_signup)
    db.session.commit()
 
    return jsonify(message="Signup successful!")
 
if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/validate', methods=['POST'])
# def validate():
#     try:
#         name = request.json.get('name')
#         password = request.json.get('password')

#         user = Signup.query.filter_by(name=name, password=password).first()

#         if user:
#             return jsonify({'message': 'Login successful!'})
#         else:
#             return jsonify({'error_message': 'Invalid name or password.'}), 400

#     except Exception as e:
#         return jsonify({'error_message': str(e)}), 500

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)