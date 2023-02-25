'----------------------------------------------------jwt - json web token----------------------------------------------------'
import time
import jwt

SEKRET_KEY = 'n0)(tms7g+i%l5bh(=poc0b8k1lwl=7996a(_=skermenk^=u3'
ALGO = 'HS256'
ACCEESS_TOKEN_EXPIRE =  5 #SEKUND
REFRESH_TOKEN_EXPIRE = 30


def encodeJWY(data):
    payload_access ={
        'data':data,
        'expiry':time.time() + ACCEESS_TOKEN_EXPIRE
    }
    payload_refresh ={
        'data':data,
        'expiry':time.time()+REFRESH_TOKEN_EXPIRE
    }

    access_token = jwt.encode(payload_access, SEKRET_KEY, algorithm=ALGO)
    refresh_token = jwt.encode(payload_refresh, SEKRET_KEY, algorithm=ALGO)
    return {'access':access_token, 'refresh':refresh_token}

def decodeJWT(token:str):
    try:
        decoded = jwt.decode(token, SEKRET_KEY,algorithms=[ALGO])
        if decoded['expiry'] >= time.time(): #esli srok godnosti eshe ne istek
            return decoded
        return {}
    except:
        return {}

def refreshJWT(refresh:str):
    decoded = decodeJWT(refresh)
    if decoded:
        return encodeJWY(decoded['data'])
    return{}











