from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Home page for the Video Page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
