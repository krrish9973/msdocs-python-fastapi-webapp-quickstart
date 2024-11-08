from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')  # Specify the template folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/api")
def api():
    return '{"message": "Hello, World!"}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)