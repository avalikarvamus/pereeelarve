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
    if request.method == 'POST':
        data = dict((key, request.form.getlist(key)
                    if len(request.form.getlist(key)) > 1
                    else request.form.getlist(key)[0])
                        for key in request.form.keys())
        budget = Budget()
        print data
        form.populate_obj(budget)
        #budget.incomings.append(BudgetLine(name=data["incomename0"], estimate=float(data["incomeestimate0"])))
        #budget.spendings.append(BudgetLine(name=data["spendingname0"], estimate=float(data["spendingestimate0"])))
        for i in range(0, 10):
            incomename = None
            incomeestimate = None
            incomename = data.get("incomename"+str(i), None)
            incomeestimate = data.get("incomeestimate"+str(i), None)
            try:
                if incomeestimate:
                    estimate = float(incomeestimate)
                else:
                    estimate = None
            except ValueError,e:
                print "error",e, "'"+incomeestimate+"' is not float number!"
                estimate = None
            if incomename and incomeestimate:
                budget.incomings.append(BudgetLine(name=incomename, estimate=estimate))
        for i in range(0, 10):
            spendname = None
            spendestimate = None
            spendname = data.get("spendingname"+str(i), None)
            spendestimate = data.get("spendingestimate"+str(i), None)
            try:
                if spendestimate:
                    estimate = float(spendestimate)
                else:
                    estimate = None
            except ValueError,e:
                print "error",e, "'"+spendestimate+"' is not float number!"
                estimate = None
            if spendname and spendestimate:
                budget.spendings.append(BudgetLine(name=spendname, estimate=estimate))

        db.session.add(budget)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("add_budget.html", title = 'Lisa pereeelarve', form = form)

@app.route('/')
def index():
    #if 'user' in session:
    budgets = Budget.query.all()
    return render_template("index.html", title = 'Pereeelarved', budgets = budgets)
    #return render_template("loginform.html", title = 'Login: Pereeelarve')


app.secret_key="asdasq3424qwerqwr35446wef6w4d4f56ds46ae8r42385+fr6we541"

