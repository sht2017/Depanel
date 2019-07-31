import hashlib,base64,uuid,random
def generateRandom():
    return hashlib.sha1(hashlib.sha3_512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest().encode(encoding="utf-8")).hexdigest()

def generateKey():
    key0=hashlib.blake2b(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key1=hashlib.md5(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key2=hashlib.sha384(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key3=hashlib.blake2s(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key4=hashlib.sha1(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key5=hashlib.sha256(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key6=hashlib.sha512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key7=hashlib.sha3_256(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key8=hashlib.sha3_512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    key9=hashlib.sha3_384(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest()
    with open('.key','w',encoding='utf-8') as do:
        do.write(locals()['key'+str(random.randint(0,9))])

def gcrypt(source):
    return hashlib.sha1(hashlib.sha3_512(base64.b64encode(str(source).encode(encoding="utf-8"))).hexdigest().encode(encoding="utf-8")).hexdigest()