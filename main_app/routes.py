 # import necessary file for application
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash

# though we use @app.route so we need to import app variable which is diclare in __init__.py
from main_app import app

# import custom form field from form.py
from main_app.form import AdmissionForm 
from main_app.form import LoginForm
from main_app.form import ApplyTeacherForm
from main_app.form import ApplyParentsForm
from main_app.form import LoginFormParents

# import database models from models.py



#   default route of web app
@app.route('/')
def index():
    return render_template('index.html')

#   admission route
@app.route('/admission', methods=['POST', 'GET'])
def admission():
    form = AdmissionForm()
    return render_template('admission.html', form=form)

#   apply for teacher route
@app.route('/teacher/apply', methods=['POST', 'GET'])
def applyTeacher():
    form = ApplyTeacherForm()
    return render_template('apply_teacher.html', form=form)

#   apply for parents route
@app.route('/parents/apply', methods=['POST', 'GET'])
def applyParents():
    form = ApplyParentsForm()
    return render_template('apply_parents.html', form=form)

#   login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

#   login as parents route
@app.route('/parents/login', methods=['POST', 'GET'])
def loginParents():
    form = LoginFormParents()
    return render_template('login_parents.html', form=form)


#   about us route
@app.route('/about')
def about():
    return render_template('about.html')