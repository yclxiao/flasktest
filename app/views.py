from app import flaskApp
from flask import render_template,request
from app.models import Todo

@flaskApp.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("index.html", todos = todos)

@flaskApp.route('/add',methods=['POST'])
def add():
    content = request.form.get('content')
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos = todos)

@flaskApp.route('/done/<string:todo_id>')
def done(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@flaskApp.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@flaskApp.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)

@flaskApp.errorhandler(404)
def not_found(e):
    return render_template("404.html"),404
