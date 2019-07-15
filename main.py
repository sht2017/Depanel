from flask import Flask,render_template,redirect,abort
import base64,uuid

app = Flask(__name__)
randomLoginPath = ''
def generateRandomLoginUrl():
    global randomLoginPath
    randomLoginPath=base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8")).decode()
    print('生成'+randomLoginPath)

@app.route('/')
def index():
    return 'aaawsl'

@app.route('/login/')
def redLogin():
    generateRandomLoginUrl()
    return redirect('/login/'+randomLoginPath)

@app.route('/login/<path>')
def login(path=None):
    if path==randomLoginPath:
        generateRandomLoginUrl()
        return render_template('login.html')
    else:
        abort(410)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')