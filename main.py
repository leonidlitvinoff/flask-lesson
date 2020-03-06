from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    config = {'title': prof}
    if 'инженер' in prof.lower():
        config['special_title'] = 'Инженерные тренажеры'
        config['img_url'] = url_for('static', filename='img/engener.jpg')
    elif 'науч' in prof.lower():
        config['special_title'] = 'Научные симуляторы'
        config['img_url'] = url_for('static', filename='img/doctor.jpg')
    else:
        config['special_title'] = 'Общая комната'
        config['img_url'] = url_for('static', filename='img/alls.jpg')

    return render_template('training.html', **config)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')