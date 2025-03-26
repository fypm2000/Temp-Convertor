# Temp-Convertor
Build and run a simple web application as a Docker container.
from flask import Flask, render_template
import traceback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/c2f/<value>")
def convert_to_fahrenheit(value):
    try:
        celsius = float(value)
        fahrenheit = round(celsius * 9/5 + 32, 3)
        return render_template('convert1.html', var1=value, var2=fahrenheit)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a number.")

@app.route("/f2c/<value>")
def convert_to_celsius(value):
    try:
        fahrenheit = float(value)
        celsius = round((fahrenheit - 32) * 5/9, 3)
        return render_template('convert2.html', var1=value, var2=celsius)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a number.")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
