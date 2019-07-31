def failed(username,password):
    import os,generate
    from crypt import crypt
    if os.path.isfile('./admin/'+username+'.key'):
        with open('./admin/'+username+'.key','r',encoding="utf-8") as file:
            key=file.read()
        if generate.gcrypt(crypt(username+'&'+password))==key:
            return bool(False)
        else:
            return bool(True)
    else:
        return bool(True)
'''    import generate
    from crypt import crypt
    with open('./help/'+str('.key'),'r',encoding="utf-8") as file:
        key=file.read()
    if generate.gcrypt(crypt(username+'&'+password))=='1':
        return bool(True)
    else:
        return bool(False)'''

def reject(username,password):
    if username == '' and password == '':
        return '用户名和密码不得为空'
    elif username == '':
        return '用户名不得为空'
    elif password == '':
        return '密码不得为空'
    else:
        return bool(False)