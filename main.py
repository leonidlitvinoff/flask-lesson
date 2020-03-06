from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    config = {'title': 'Каюты'}
    if sex == 'female' and age >= 21:
        config['color'] = url_for('static', filename='img/female_grand.jpg')
        config['person'] = url_for('static', filename='img/big.jpg')
    elif sex == 'female' and age < 21:
        config['color'] = url_for('static', filename='img/female_small.jpg')
        config['person'] = url_for('static', filename='img/small.jpg')
    elif sex == 'male' and age < 21:
        config['color'] = url_for('static', filename='img/male_small.jpg')
        config['person'] = url_for('static', filename='img/small.jpg')
    else:
        config['color'] = url_for('static', filename='img/male_grand.jpg')
        config['person'] = url_for('static', filename='img/big.jpg')
    return render_template('table.html', **config)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')