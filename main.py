from flask import Flask,render_template,redirect,abort,request,flash
from loginCheck import valid_login
from generateRandom import generateRandomLoginUrl
from helpRenderer import renderHelp

app = Flask(__name__)
app.config['SECRET_KEY'] = generateRandomLoginUrl()

@app.route('/')
def index():
    return redirect('/login/')
#    return 'aaawsl'

@app.route('/login/',methods=['GET', 'POST'])
def login(error='',title='Depanel Login'):
    if request.method=='POST':
        print(request.form['username'],request.form['passphrase'])
        if request.form['username']=='' and request.form['passphrase']=='':
            error='用户名和密码不得为空'
        elif request.form['username']=='':
            error='用户名不得为空'
        elif request.form['passphrase']=='':
            error='密码不得为空'
        else:
            if valid_login(request.form['username'],request.form['passphrase']):
                print('valid')
            else:
                error='Invalid username/password'
    return render_template('login.html',error=error,title=title)

@app.route('/help/retrievePassword/')
def retrievePassword():
    retrievePassword=renderHelp('retrievePassword')
    return render_template('help.html',title=retrievePassword[0],author=retrievePassword[1],content1=retrievePassword[2],content2=retrievePassword[3],content3=retrievePassword[4])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')