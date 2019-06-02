from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
                    TextAreaField, DecimalField, DateField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username    = StringField('Имя', validators=[DataRequired()])
    password    = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit      = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username  = StringField('Имя', validators=[DataRequired()])
    email     = StringField('Почта', validators=[DataRequired(), Email()])
    password  = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit    = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Воспользуйтель другим именем')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Почта уже используется')

class ProjectForm(FlaskForm):
    name = StringField('Название проекта', validators=[DataRequired()])
    description = TextAreaField('Описание проекта', validators=[DataRequired()])
    participants = StringField('Участники', validators=[DataRequired()])
    budget = DecimalField('Бюджет', validators=[DataRequired()])
    beginning = DateField('Начало проекта', format='%d.%m.%Y', validators=[DataRequired()])
    end = DateField('Конец проекта', format='%d.%m.%Y', validators=[DataRequired()])
