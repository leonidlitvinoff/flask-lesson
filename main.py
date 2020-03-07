from flask import Flask, render_template, url_for, redirect, request
import json
app = Flask(__name__)


@app.route('/member')
def member():
    config = {'title': 'Member',
              'persons': json.load(open('templates\\command.json'))}
    return render_template('member.html', **config)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')