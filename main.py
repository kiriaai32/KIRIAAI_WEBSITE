from flask import Flask, render_template, request, send_from_directory
from forms import CalculatorForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            input_wallet = float(request.form['input_wallet'])
            rate = float(request.form['rate'])
            result = input_wallet * rate
        except ValueError:
            result = "Please enter valid numbers."
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

# make calculator work
# make a section for video
# create a custom cursor
# make the background music work
