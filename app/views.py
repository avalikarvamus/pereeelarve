# -*- coding: utf-8 -*-
#
#    Copyright 2014 Madis Veskimeister <madis@pingviinitiivul.ee>
#

import  os, random, exceptions
from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from models import User, Budget, BudgetLine
from forms import AddBudgetForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.has_key('kasutaja') and request.form.has_key('salakala'):
            clName = request.form['kasutaja']
            clPass = request.form['salakala']
            user = User.query.filter(User.name==clName and User.password==encrypt_password(clPass)).all()
            if user:
                session['user']=user
                return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form.has_key('kasutaja') and request.form.has_key('salakala'):
            print "blablaa"
    #form = UserRegistrationForm()
    return render_template("register.html")

@app.route('/example')
def example():
    budget = Budget.query.first()
    return render_template("budget.html", title = 'Pereeelarve', budget = budget)

@app.route('/eelarve/<int:budget_id>')
def show_budget(budget_id):
    #if 'user' in session:
    budget = Budget.query.filter(Budget.id==budget_id).first()
    return render_template("budget.html", title = 'Pereeelarve', budget = budget)
    #return render_template("loginform.html", title = 'Login: Pereeelarve')

@app.route('/lisa-eelarve/', methods = ['GET', 'POST'])
def add_budget():
    form = AddBudgetForm()
    return render_template("add_budget.html", title = 'Lisa pereeelarve', form = form)

@app.route('/')
def index():
    #if 'user' in session:
    budgets = Budget.query.all()
    return render_template("index.html", title = 'Pereeelarved', budgets = budgets)
    #return render_template("loginform.html", title = 'Login: Pereeelarve')


app.secret_key="asdasq3424qwerqwr35446wef6w4d4f56ds46ae8r42385+fr6we541"
	
