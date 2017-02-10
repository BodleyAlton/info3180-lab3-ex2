from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class contactForm(FlaskForm):
    name= StringField(u'name', validators=[InputRequired()])
    email= StringField(u'email', validators=[InputRequired()])
    subject=StringField(u'subject', validators=[InputRequired()])
    message=StringField(u'message', validators=[InputRequired()])
