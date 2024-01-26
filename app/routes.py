from app import app
from flask import render_template
from app.form import PasswordForm
from random import choice,randint
from string import ascii_lowercase,ascii_uppercase
from config import Config



@app.route('/',methods=["GET",'POST'])
def generate_password():
    generate_password = [(choice(ascii_lowercase),choice(ascii_uppercase),choice(Config.SPECIAL_CHAR),choice(Config.NUMBER))[randint(0,3)] for i in range(8)]
    generate_password = ''.join(generate_password)
    form = PasswordForm(password=generate_password)
    if form.validate_on_submit():
        count = form.range_decimal.data
        if form.special_char.data and form.number.data:
            generate_password = [(choice(ascii_lowercase),choice(ascii_uppercase),choice(Config.SPECIAL_CHAR),choice(Config.NUMBER))[randint(0,3)] for i in range(count)]
        elif form.special_char.data:
            generate_password = [(choice(ascii_lowercase),choice(ascii_uppercase),choice(Config.SPECIAL_CHAR))[randint(0,2)] for i in range(count)]
        elif form.number.data:
            generate_password = [(choice(ascii_lowercase),choice(ascii_uppercase),choice(Config.NUMBER))[randint(0,2)] for i in range(count)]
        else:
            generate_password = [(choice(ascii_lowercase),choice(ascii_uppercase))[randint(0,1)] for i in range(count)]
        generate_password = ''.join(generate_password)
        form.password.data = generate_password
    return render_template('generate_password.html',form=form)