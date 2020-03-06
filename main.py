from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'z6EQt3NM6sdbT4nic11ZvvQK4PhvDRGZ0B9BgRLtDKxmdMdjLJvQ4wFjbAQV44i30SQEOnJKpcMdLIxf'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
COMMAND = {'Peoples': {'1': {'pass': 'asd123'},
                       '2': {'pass': 'qwerty564'},
                       '3': {'pass': 'poiuy0009'}},
           'Captain': {'id': '0', 'pass': '1234567890'}}

class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_captain = StringField('Id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global COMMAND
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data in COMMAND['Peoples'].keys():
            if form.password.data == COMMAND['Peoples'][form.username.data]['pass']:
                if form.username_captain.data == COMMAND['Captain']['id']:
                    if form.password_captain.data == COMMAND['Captain']['pass']:
                        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form, css_url=url_for('static', filename='css/style.css'))

@app.route('/success')
def success():
    return render_template('success.html', title='Авторизация')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')