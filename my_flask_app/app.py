from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def any_function():
    return render_template('index.html')

@app.route('/name')
def name():
    return render_template('name.html')

if __name__ == '__main__':
    app.run(debug=True)
