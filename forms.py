
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный Email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100, message=("расия лох Украина топ"))])
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")])
    email = StringField("Email: ", validators=[Email("Некорректный Email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100, message=("расия лох Украина топ"))])
    psw2 = PasswordField("Повтор пароля: ", validators=[DataRequired(), EqualTo('psw', message="Пароли не совпадают")])
    submit = SubmitField("Регистрация")
