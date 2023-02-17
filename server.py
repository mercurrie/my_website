from flask import Flask, render_template

HTML_PATH = "mason.html"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template(HTML_PATH)


if __name__ == "__main__":
    app.run(debug=True)
