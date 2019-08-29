import base64
from Crypto.Cipher import AES


def pkcs7padding(text):
    bs = AES.block_size
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]


def encrypt(content):
    key_bytes = bytes(getKey(), encoding='utf-8')
    iv = bytes(getIvKey(), encoding='utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    content_padding = pkcs7padding(str(content))
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result

def getKey():
    with open('.key','r',encoding='utf-8') as do:
        key=do.read()
    if int(str(len(key)/16).split('.')[0]) == 0:
        while len(key)<16:
            key=key+''
    elif int(len(key)%16) != 0:
        key=key[0:16]
    elif int(len(key)%24) != 0:
        key=key[0:24]
    elif int(len(key)%32) != 0:
        key=key[0:32]
    elif int(len(key))>32:
        key=key[0:32]
    return key

def getIvKey():
    with open('.key','r',encoding='utf-8') as do:
        key=do.read()
    if int(str(len(key)/16).split('.')[0]) == 0:
        while len(key)<16:
            key=key+''
    elif len(key)>16:
        key=key[-16:]
    return key

def crypt(source):
    return encrypt(source)
