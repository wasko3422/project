from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProjectForm
from app.models import User, Project


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            budget=form.budget.data,
            participants=form.participants.data,
            beginning=form.beginning.data,
            end=form.end.data,
            leader=current_user.username,
            leader_id=current_user.id,
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('projects'))

    
    return render_template('add.html', form=form)

@app.route('/plans')
@login_required
def plans():
    return render_template('plans.html')

@app.route('/projects')
@login_required
def projects():
    projects = Project.query.filter_by(leader_id=current_user.id)
    return render_template('projects.html', projects=projects)

@app.route('/results')
@login_required
def results():
    return render_template('results.html')


@app.route('/register',  methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # TODO flash()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

