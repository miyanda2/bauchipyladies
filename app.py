from flask import Flask, render_template, redirect, url_for, flash, session, request

app = Flask(__name__)




# renders a home page
@app.route('/')
def index():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)