from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    print(url_for('static', filename='img/female_grand.jpg'))
    config = {'title': 'Каюты',
              'sex': sex,
              'age': age}
    return render_template('table.html', **config)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')