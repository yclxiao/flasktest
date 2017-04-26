# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from app import flaskApp
from app.models import Todo

manager = Manager(flaskApp)

manager.add_command("runserver",
         Server(host='0.0.0.0',port=5000, use_debugger=True))

@manager.command
def save_todo():
    todo = Todo(content="my first todo1")
    todo.save()

if __name__ == '__main__':
    manager.run()