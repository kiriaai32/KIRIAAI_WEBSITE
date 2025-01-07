from flask import Flask, render_template, request, send_from_directory
from forms import CalculatorForm
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    string = "We are still developing it. It is going to take some time"
    if request.method == 'POST':
        try:
            result = string
        except ValueError:
            result = "Please enter valid numbers."
    return render_template('index.html', result=result, string=string)


if __name__ == '__main__':
    app.run(debug=True)

# make calculator work
# make a section for video
# create a custom cursor
# make the background music work
