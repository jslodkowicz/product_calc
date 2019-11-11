from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired


class CalcForm(FlaskForm):
    quantity = IntegerField('How many products?', validators=[DataRequired()])
    price = FloatField('Product price', validators=[DataRequired()])
    state = SelectField('State', choices=[
        ('UT','Utah'), ('NV', 'Nevada'), ('TX', 'Texas'), ('AL', 'Alabama'), ('CA', 'California')])
    submit = SubmitField('Calculate')