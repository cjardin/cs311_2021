import hashlib
from itertools import product
import binascii


#print(hashlib.sha256("heeelllo1".encode('utf-8')).hexdigest())

#print(hashlib.sha256("heeelllo1".encode('utf-8')).digest()[1])

perm = product(list(range(256)), repeat=2)

MODS = 10
MY_MOD = 2

count = 0
for p in perm:

    count += 1
    if count % MODS != MY_MOD:
        continue 
    print(binascii.hexlify(bytearray(p)))
    #coin_hash = hashlib.sha256(bytes( p )).digest()
    #if coin_hash[0] == 1 and coin_hash[1] == 1:
    #    print("found one")



