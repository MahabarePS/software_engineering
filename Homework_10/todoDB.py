from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date)
    finish_date = db.Column(db.Date)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todos_data = []
    for todo in todos:
        todo_data = {
            "id": todo.id,
            "task": todo.task,
            "start_date": str(todo.start_date) if todo.start_date else None,
            "finish_date": str(todo.finish_date) if todo.finish_date else None
        }
        todos_data.append(todo_data)
    return jsonify(todos_data)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todo = Todo(task=data['task'], start_date=data['start_date'], finish_date=data['finish_date'])
    db.session.add(todo)
    db.session.commit()
    return "Todo added successfully", 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)
    if todo is None:
        return jsonify({"message": "Todo not found"}), 404
    try:
        data = request.get_json()
        if 'start_date' in data:
            todo.start_date = data['start_date']
        if 'finish_date' in data:
            todo.finish_date = data['finish_date']
        db.session.commit()
        return jsonify({"message": "Todo updated successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return "Todo deleted successfully", 200
    else:
        return "Todo not found", 404

# Other routes and functionalities can be added as per requirements

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
