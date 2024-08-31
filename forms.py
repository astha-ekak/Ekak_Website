from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,Email,ValidationError

class ContactForm(FlaskForm):
    """Contact Form For Argus Website . 

    """
    name=StringField("Name",validators=[DataRequired(),Length(min=4,max=30)])
    email=EmailField("Email",validators=[DataRequired(),Length(min=6,max=35),Email()])
    mobile=StringField("Mobile",validators=[Length(min=10,max=10)])
    individual=StringField("Individual/Company")
    company_name=StringField("Company Name")
    purpose=StringField("Purpose")
    help=TextAreaField("How Can we Help you",validators=[DataRequired()])
    submit=SubmitField("Submit")

