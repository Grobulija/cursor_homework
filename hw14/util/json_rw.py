import json
from flask import request


def write(todos, todo_id):
    todos[todo_id] = request.json.get('text')
    data = {todo_id: todos[todo_id]}
    with open('data/todo_' + str(todo_id) + '.json', 'w') as write_file:
        json.dump(data, write_file)
    write_file.close()
    return data


def read(todo_id):
    with open('data/todo_' + str(todo_id) + '.json', 'r') as read_file:
        data = json.load(read_file)
    read_file.close()

