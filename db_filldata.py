#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright 2014 Madis Veskimeister <madis@pingviinitiivul.ee>
#

from app.config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path
from app.models import User, Budget, BudgetLine
from flask.ext.security.utils import encrypt_password

def fillData():
    #toomas = User(name="Vana", firstname="Toomas", email="toomas@utoopia.eu", password=encrypt_password("123test"))
    #db.session.add(toomas)
    myspendings = [BudgetLine(name="Kommunaalid", estimate=50.0),BudgetLine(name="Toit", estimate=220.0), BudgetLine(name="Bensiin", estimate=150.0),BudgetLine(name="Kommunikatsioonid", estimate=12.0)]
    myincomings = [BudgetLine(name="Palk", estimate=600.0)]
    budget = Budget(name="test", desc="kirjeldus", incomings=myincomings, spendings=myspendings)
    myspendings2 = [BudgetLine(name="Kommunaalid", estimate=45.0), BudgetLine(name="Toit", estimate=320.0), BudgetLine(name="Bussipiletid", estimate=99.0),BudgetLine(name="Kommunikatsioonid", estimate=32.0)]
    myincomings2 = [BudgetLine(name="Palk", estimate=400.0), BudgetLine(name="Dividendid", estimate=280.0)]
    budget2 = Budget(name="test2", incomings=myincomings2, spendings=myspendings2)
    myspendings3 = [BudgetLine(name="Kommunaalid", estimate=65.0), BudgetLine(name="Toit", estimate=280.0), BudgetLine(name="Bensiin", estimate=159.0),BudgetLine(name="Auto remont", estimate=320),BudgetLine(name="Kommunikatsioonid", estimate=42.0)]
    myincomings3 = [BudgetLine(name="Palk", estimate=350.0), BudgetLine(name="Dividendid", estimate=240.0)]
    budget3 = Budget(name="test3", desc="l6hkine eelarve", incomings=myincomings3, spendings=myspendings3)
    db.session.add(budget)
    db.session.add(budget2)
    db.session.add(budget3)
    db.session.commit()

fillData()
