from flask import Flask, render_template
import traceback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/c2f/<value>")
def convert_temperature(value):
    try:
        # Correct Celsius to Fahrenheit conversion
        celsius = float(value)
        fahrenheit = round((celsius * 9/5) + 32, 3)  # Precise conversion formula
        return render_template('convert1.html', var1=value, var2=fahrenheit)
    except ValueError:
        # Improved error handling with a specific error message
        return render_template('index.html', error="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
