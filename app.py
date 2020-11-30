from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    url = request.form.get('urlname')
    shorturl = pyshorteners.Shortener().tinyurl.short(url)
    return render_template('result.html', shorturl=shorturl)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
