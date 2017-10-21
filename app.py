from flask import Flask
app = Flask(__name__)

@app.route('/callback')
def callback():
    return 'Welcome back!'
