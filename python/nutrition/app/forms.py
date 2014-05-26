from flask.ext.wtf import Form
from wtforms import Form, BooleanField, PasswordField, validators
from wtforms import DecimalField, TextField, IntegerField
from wtforms.validators import Required

#class ProfileForm(Form):
    #calorie_goal = IntegerField()
   # protein_goal = IntegerField()
    #carbohydrate_goal = IntegerField()
    #fat_goal = IntegerField()



class LoginForm(Form):
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    

class ProfileForm(Form):
    calorie_goal = DecimalField('Calorie Goal')
    protein_goal = DecimalField('Protein Goal')
    carbohydrate_goal = DecimalField('Carbohydrate Goal')
    fat_goal = DecimalField('Fat Goal')







    




