from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'We have finished the PFA project'
