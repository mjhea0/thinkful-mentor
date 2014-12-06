from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required

class LoginForm(Form):
    oid_provider = SelectField(u'OpenId Provider', choices=[
        ('google', 'Google'), 
        ('yahoo', 'Yahoo'), 
        ('myOpenId', 'My Open Id')])
    
