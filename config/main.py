import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    if username:
        return redirect(url_for('greet', username=username))
    return redirect(url_for('home'))

@app.route('/greet/<username>')
def greet(username):
    return render_template('greet.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))