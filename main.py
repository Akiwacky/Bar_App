from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/story')
def about_me():
    return render_template('story.html')


@app.route('/menu', methods=['GET'])
def menu_item():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)