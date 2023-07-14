from flask import Flask, render_template
import 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input_data():
    return render_template('input.html')