# -*- coding: utf-8 -*-
"""

"""

from wtforms.validators import Length, Required, Email, EqualTo
from wtforms import TextField, PasswordField, \
    SubmitField, HiddenField, BooleanField, ValidationError, Field, validators

from flask import flash
from flask import request, current_app
from flask_wtf import Form
from app import db, config

from app.models import Budget

class AddBudgetForm(Form):
    name = TextField(u"Name", [Required()])
    desc = TextField(u"Description", [Required()])
    
