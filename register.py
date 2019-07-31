def in_(username,password):
    import generate
    from crypt import crypt
    generate.generateKey()
    with open('./admin/'+username+'.key', 'w',encoding='utf-8') as do:
        do.write(generate.gcrypt(crypt(username+'&'+password)))

def reject(username,password):
    import os
    if username == '' and password == '':
        return '用户名和密码不得为空'
    elif username == '':
        return  '用户名不得为空'
    elif password == '':
        return  '密码不得为空'
    elif len(username) <3:
        return  '用户名不得少于3位'
    elif len(password) <6:
        return  '密码不得少于6位'
    elif os.path.isfile('./admin/'+username+'.key'):
        return '错误！请删除./admin下所有后缀名为.key的文件'
    else:
        return bool(False)