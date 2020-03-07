from flask import Flask, render_template, url_for, redirect, request
import os
app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    config = {'title': 'Красная планета'}
    if request.method == 'POST':
        f = request.files['file']
        with open(f'static\\img\\slides\\{f.filename}', 'wb') as doc:
            doc.write(f.read())
    config['slides'] = [f'static\\img\\slides\\{i}' for i in os.listdir('static\\img\\slides\\')]
    return render_template('galery.html', **config)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')