import register,login
from flask import Flask, render_template, redirect, abort, request, session
from checkIfInstalled import installed
from generate import generateRandom
from helpRenderer import renderHelp

app = Flask(__name__)
app.config['SECRET_KEY'] = generateRandom()

@app.route('/')
def index():
    if not installed():
        return redirect('/install/')
    if 'username' in session:
        return render_template('index.html',user=(session['username']))
    return redirect('/login/')

@app.route('/login/', methods=['GET', 'POST'])
def login_(error='', title='Depanel Login'):
    ip = request.remote_addr
    if not installed():
        return redirect('/')
    elif 'username' in session:
        return redirect('/')
    elif request.method == 'POST':
        username = str(request.form['username'])
        password = str(request.form['password'])
        reject=login.reject(username, password)
        if reject:
            error=reject
            print('用户 '+username+' 登入被拒绝 原因是 '+error+' ip地址是 '+ip)
        else:
            if login.failed(username, password):
                error = 'Invalid username/password'
                print('用户 '+username+' 登入被拒绝 原因是 '+error+' ip地址是 '+ip)
            else:
                print('用户 '+username+' 登入成功'+' ip地址是 '+ip)
                session['username']=username
                return redirect('/')
    return render_template('login.html', error=error, title=title)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/help/<parameter>/')
def help(parameter):
    if not installed():
        return redirect('/')
    print(parameter)
    rHelp = renderHelp(parameter)
    return render_template('help.html', title=rHelp[0], author=rHelp[1], content1=rHelp[2], content2=rHelp[3], content3=rHelp[4], content4=rHelp[5], content5=rHelp[6])    

@app.route('/install/')
def install():
    if not installed():
        return render_template('install/install.html')
    return redirect('/')

@app.route('/install/step1/')
def step1():
    if not installed():
        return render_template('install/userArgeement.html')
    return redirect('/')

@app.route('/install/step2/')
def step2():
    if not installed():
        return render_template('install/privacyAndTerms.html')
    return redirect('/')

@app.route('/install/step3/', methods=['GET', 'POST'])
def register_(error=''):
    if not installed():
        if request.method == 'POST':
            username = str(request.form['username'])
            password = str(request.form['password'])
            reject=register.reject(username, password)
            if reject:
                error=reject
            else:
                register.in_(username,password)
                return redirect('/')
        return render_template('install/register.html', error=error)
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
