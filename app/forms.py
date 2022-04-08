# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Optional

class UploadForm(FlaskForm):
    description=TextAreaField("Description",validators=[DataRequired()])
    photo=FileField('File Upload',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
