from flask import Flask, render_template, request, redirect, url_for
from calculator import quadratic

app = Flask(__name__)


app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = name.upper()
    return render_template('hello.html', name=name)


@app.route('/calculator/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        root_1, root_2 = quadratic(a, b, c)
        if root_1:
            return render_template('calculator_result.html', a=a, b=b, c=c,
                                   root_1=root_1, root_2=root_2)
    return render_template('calculator_form.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
