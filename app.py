from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/vaccination')
def vaccination():
    return render_template('vaccination.html')


if __name__ == "__main__":
    app.run(debug=True)
