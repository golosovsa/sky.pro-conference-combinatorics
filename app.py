from flask import Flask, render_template


from model import AppPage


app = Flask(__name__)


@app.route('/')
def app_index():  # put application's code here
    app_page = AppPage()
    return render_template("index.html", app_page=app_page)


if __name__ == '__main__':
    app.run()
