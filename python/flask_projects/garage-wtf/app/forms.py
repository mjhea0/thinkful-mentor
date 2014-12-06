from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField
from wtforms.validators import Required, NumberRange, Regexp

mfg_options =  [('not specified', 'not specified'),('mini', 'Mini'), ('porsche', 'Porsche'), ('saab', 'Saab')]

class CarDetailsForm(Form):
    color = TextField('color', validators=[Required()])
    model = TextField('model', validators=[Required()])
    year = IntegerField('year', validators=[NumberRange(min=1900, max=2020)])
    mfg = SelectField(u'Manufacturer', choices=mfg_options,
        validators=[Required()])

class CarFilterForm(Form):
    mfg = SelectField(u'Manufacturer', choices=mfg_options)
