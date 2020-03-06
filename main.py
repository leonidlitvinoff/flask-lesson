from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    config = {'title': 'Анкета',
              'surname': 'Беркут',
              'name': 'Крылов',
              'education': '3 Высшее',
              'profession': 'Экзобиолог',
              'sex': 'Мужской',
              'motivation': 'Отсутствие мотивации, тревожность и конфликтность.',
              'ready': 'Да',
              'css_url': url_for('static', filename='css/style.css')}
    return render_template('auto_answer.html', **config)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')