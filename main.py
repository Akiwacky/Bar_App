from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from get_menu import FetchItems

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
    fetch_items = FetchItems()
    fetch_items.get_items()
    return render_template('menu.html', items=fetch_items.items)


if __name__ == '__main__':
    app.run(debug=True)