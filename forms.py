from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired

class CalculatorForm(FlaskForm):
    first_input = FloatField('Enter the number', validators=[InputRequired()])
    second_input = FloatField('Enter the rate', validators=[InputRequired()])
    submit = SubmitField('Calculate')
