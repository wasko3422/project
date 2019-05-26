from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/base')
def base():
    return render_template('base.html')
