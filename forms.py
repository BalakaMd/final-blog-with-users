from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, ValidationError
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter correct email.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sing me Up!')

    @staticmethod
    def validate_password(self, field):
        password = field.data
        if len(password) < 8 or not any(char.isdigit() for char in password):
            raise ValidationError('The password must contain at least 8 letters and at least one number.')

    @staticmethod
    def validate_name(self, field):
        name = field.data
        if len(name) < 4:
            raise ValidationError('The name must contain at least 4 letters.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter correct email.')],
                        render_kw={"placeholder": "email@example.com"})
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sing me Up!')


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment")
    submit = SubmitField('Submit comment')
