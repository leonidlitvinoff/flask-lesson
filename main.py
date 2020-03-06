from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
COMMAND = ['Артем',
           'Максим Кадулин',
           'Сергей Смирнов',
           'Андрей Васильков']


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', title='Каюты', data=COMMAND, length=len(COMMAND))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')