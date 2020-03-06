from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/list_prof/<type>')
def list_prof(type):
    config = {'data': ['Инженер-исследователь',
                       'Пилот',
                       'Строитель',
                       'Экзобиолог',
                       'Врач',
                       'Климатолог']}
    if type != 'ol' and type != 'ul':
        config['type'] = 'Неверный тип'
        return 'Error'
    config['type'] = type
    return render_template('list_prof.html', **config)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')