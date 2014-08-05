# -*- coding: utf-8 -*-
#
#    Copyright 2014 Madis Veskimeister <madis@pingviinitiivul.ee>
#

from flask import Flask
from app import app, db
from datetime import datetime
from sqlalchemy.orm import relationship, backref

incomings_rel = db.Table('incomings_rel',
                             db.Column('budget_id',
                                       db.Integer,
                                       db.ForeignKey('budget.id')),
                             db.Column('budgetline_id',
                                       db.Integer,
                                       db.ForeignKey('budgetline.id'))
                             )

spendings_rel = db.Table('spendings_rel',
                             db.Column('budget_id',
                                       db.Integer,
                                       db.ForeignKey('budget.id')),
                             db.Column('budgetline_id',
                                       db.Integer,
                                       db.ForeignKey('budgetline.id'))
                             )

class User(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(), nullable=False)
    firstname = db.Column(db.String(), nullable=False)
    email     = db.Column(db.String(), nullable=False)
    time_added_to_base = db.Column(db.DateTime(timezone=True), default=db.func.now())
    password  = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return 'kasutaja %s, %s ( %s , %s )' % self.name, self.firstname, self.email, self.time_added_to_base.strftime('%d.%m.%y %H:%M')


class BudgetLine(db.Model):
    __tablename__    = 'budgetline'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    estimate = db.Column(db.Float)


class Budget(db.Model):
    __tablename__    = 'budget'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    time_added_to_base = db.Column(db.DateTime(timezone=True), default=db.func.now())

    #owner_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #owner     = db.relationship("user", backref="budgets", lazy="joined")

    incomings = db.relationship("BudgetLine", secondary=incomings_rel, lazy="dynamic")
    spendings = db.relationship("BudgetLine", secondary=spendings_rel, lazy="dynamic")

    @property
    def total_income(self):
        sum = 0.0
        for item in self.incomings:
            if item.estimate:
                sum = sum + item.estimate
        return sum

    @property
    def total_spending(self):
        sum = 0.0
        for item in self.spendings:
            if item.estimate:
                sum = sum + item.estimate
        return sum

    @property
    def profit_or_loss(self):
        tot_income = self.total_income
        tot_spending = self.total_spending
        if tot_income < tot_spending:
            return "Loss: " + str(tot_income - tot_spending)
        elif tot_income >= tot_spending:
            return "Profit: " + str(tot_income - tot_spending)
        return "Error!"


