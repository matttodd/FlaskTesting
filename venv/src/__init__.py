from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('setcookie.html'))
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
