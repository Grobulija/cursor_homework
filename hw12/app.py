from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/calc/<int:a>/<int:b>/<string:func>')
def calc(a, b, func):
    actions = {'sum': "+", 'dif': "-", 'mult': "*", 'div': "/"}
    func_c = eval(func, actions)
    expr = str(a) + func_c + str(b)
    res = eval(expr)
    if func_c:
        if func_c == '/' and b == 0:
            return render_template('calc.html', b=b)
        return render_template('calc.html', a=a, b=b, func=func_c, result=res)
    else:
        return render_template('calc.html', func="Null")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
