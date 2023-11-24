# loginvalidate.py

from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Import the datetime module
import uuid  # Add this import statement

app = Flask(__name__)
app.secret_key = '123pari'
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root123@127.0.0.1:3306/sys'
db = SQLAlchemy(app)

class signup(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class sessiondetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    sessionid = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now, nullable=False)

@app.route('/validate1', methods=['POST'])
def validate():
    try:
        username = request.json.get('name')
        password = request.json.get('password')

        user = signup.query.filter_by(username=username, password=password).first()

        if user:
            # Set the user session
            session['user_id'] = user.userid

            # Generate a unique session ID using uuid
            session_id = str(uuid.uuid4())

            # Insert session details into the database
            new_session = sessiondetail(username=user.username, sessionid=session_id)
            db.session.add(new_session)
            db.session.commit()

            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'error_message': 'Invalid name or password.'}), 400

    except Exception as e:
        return jsonify({'error_message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
