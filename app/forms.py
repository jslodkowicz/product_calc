from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired


class CalcForm(FlaskForm):
    quantity = IntegerField("How many products?", validators=[InputRequired()])
    price = FloatField("Product price", validators=[InputRequired()])
    state = SelectField(
        "State",
        choices=[
            ("UT", "Utah"),
            ("NV", "Nevada"),
            ("TX", "Texas"),
            ("AL", "Alabama"),
            ("CA", "California"),
        ],
    )
    submit = SubmitField("Calculate")
