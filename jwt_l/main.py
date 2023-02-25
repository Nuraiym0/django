import time
from jwt_hendler import encodeJWY, decodeJWT, refreshJWT


user = {'username':'nastya','id':1}

jwt_token = encodeJWY(user) # poluchem tokeny
print(jwt_token)

time.sleep(6) #prohodit vremya
decoded = decodeJWT(jwt_token['access'])
print(decoded) # token istek



new_jwt = refreshJWT(jwt_token['refresh'])
print(new_jwt) #poluchili nowyi token















