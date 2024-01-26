from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField
from wtforms.validators import NumberRange



class PasswordForm(FlaskForm):
    password = StringField(label='password',render_kw={'placeholder':'генерация паароля'})
    range_decimal = IntegerField(validators=[NumberRange(min=8,max=25)],default=8)
    number = BooleanField(label='числа')
    special_char = BooleanField(label='специальные символы',name='special_char')
    send_settings = SubmitField(label='получить пароль')
    

    