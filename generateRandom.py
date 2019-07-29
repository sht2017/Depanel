import hashlib,base64,uuid
def generateRandomLoginUrl():
    randomLoginPath=hashlib.sha1(hashlib.sha3_512(base64.b64encode(str(uuid.uuid1()).encode(encoding="utf-8"))).hexdigest().encode(encoding="utf-8")).hexdigest()
    return randomLoginPath