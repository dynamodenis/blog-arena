from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class UploadBlog(FlaskForm):
    category=SelectField('Select Blog Category',validators=[DataRequired()],choices=[('Political Blog','Political Blog'),
                                                    ('Business Blog','Business Blog'),
                                                    ('Fashion Blog','Fashion Blog'),
                                                    ('Sports Blog','Sports Blog'),
                                                    ('Entertainment Blog','Entertainment Blog'),
                                                    ('Tech & Innovation Blog','Tech & Innovation Blog'),
                                                    ('Others','None of the above')])
    blog=TextAreaField('Write Blog Here:',validators=[DataRequired()])
    submit=SubmitField('Post Blog')