from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import send_file


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
#CORS(app, resources={r"/*": {"origins": "*"}})


# CORS(app, resources={
#     r"/": {"origins": "http://localhost:3000"},
#     r"/signInValidate": {"origins": "http://localhost:3000"},
#     r"/dashboard": {"origins": "http://localhost:3000"},
# })

# Configure the SQLAlchemy database URI for your specific database system
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Winacs%40560$$@127.0.0.1:3306/user'
db = SQLAlchemy(app)

# Define a model for the 'signup' table
class Signup(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/')
def signin():
    return render_template('SignInForm.js')

# @app.route('/signInValidate', methods=['POST'])
# def signin_user():
#     username = request.json.get['name']
#     password = request.json.get['password']

#     user = Signup.query.filter_by(username=username, password=password).first()

#     if user:
#         # redirect to dashboard.js
#         @app.route('/')
#         def dashboard():
#             return render_template('dashboard.js')
#     else:
#         @app.route('/')
#         def signin():
#             return render_template('SignInForm.js')
#         #return jsonify({'error_message': 'Invalid name or password.'}), 401
@app.route('/signInValidate', methods=['POST'])
def signin_user():
    data = request.get_json()
    username = data.get('name')
    password = data.get('password')

    user = Signup.query.filter_by(username=username, password=password).first()

    if user:
        if dashboard is None:
            return jsonify({'error_message': 'Godilo'})
        else:
            return redirect(url_for('dashboard'))  # You might also return user details/token here
    else:
        return jsonify({'error_message': 'Invalid name or password.'}), 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.js')

if __name__ == '__main__':
    app.run(debug=True)
