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
        input_wallet = request.form.get('input_wallet', '').strip()

        if len(input_wallet) == 44:
            result = string
        else:
            result = "Invalid token address"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

# make calculator work
# make a section for video
# create a custom cursor
# make the background music work
