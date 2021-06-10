from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/calc/<int:a>/<int:b>/<string:func>')
def calc(a,b,func):
    if func == 'sum':
        return render_template('calc.html', a=a, b=b, func = "+", result = a + b)
    elif func == 'dif':
        return render_template('calc.html', a=a, b=b, func = "-",result = a - b)
    elif func == 'mult':
        return render_template('calc.html', a=a, b=b, func = "*",result = a * b)
    elif func == 'div':
        if b == 0:
            return render_template('calc.html', b=b)
        else:
            return render_template('calc.html', a=a, b=b, func = "/", result = a / b)
    else:
        return render_template('calc.html', func="Null")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
