from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import InputRequired

class contactForm(FlaskForm):
    name= StringField(u'Name', validators=[InputRequired()])
    email= StringField(u'E-mail', validators=[InputRequired()])
    subject=StringField(u'Subject', validators=[InputRequired()])
    message=TextAreaField(u'Message',id="message" ,validators=[InputRequired()])
