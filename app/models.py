# -*- coding: utf-8 -*-
#
#    Copyright 2014 Madis Veskimeister <madis@pingviinitiivul.ee>
#

from flask import Flask
from app import app, db
from datetime import datetime
from sqlalchemy.orm import relationship, backref


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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    estimate = db.Column(db.Float)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    desc = db.Column(db.String())
    time_added_to_base = db.Column(db.DateTime(timezone=True), default=db.func.now())

    owner_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner     = db.relationship("user", backref="budgets", lazy="joined")

    incomings = db.relationship("BudgetLine", backref="budget", lazy="dynamic")
    spendings = db.relationship("BudgetLine", backref="budget", lazy="dynamic")

