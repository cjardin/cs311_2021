import binascii
import hashlib
from itertools import product
from multiprocessing import Pool

import sys


def mine_coin(x):
    repeat = x['repeat']
    mod_number = x['mod_number']
    mod_pos = x['mod_pos']
    ones = x['ones']

    looking_for = [1] * ones
    count=0
    perm = product(list(range(256)), repeat=repeat)
    coins_found = []
    for p in perm:
        if (count % mod_number) == mod_pos:
            coin_hash = hashlib.sha256(bytes( p )).digest()
            if list(coin_hash[0:ones]) == looking_for:
                coins_found.append(p)

    return coins_found


#print(mine_coin({'repeat' : 2, 'mod_number':1, 'mod_pos':0, 'ones':1}))

#sys.exit()



print(hashlib.sha256("heeelllo1".encode('utf-8')).hexdigest())

print(hashlib.sha256("heeelllo1".encode('utf-8')).digest()[1])


sys.exit()
NUMBER_OF_BYTES = 3
ONES = 1
looking_for = [1] * ONES

perm = product(list(range(256)), repeat=NUMBER_OF_BYTES)
#print(len(list(perm)))
for p in perm:
    #print(binascii.hexlify(bytearray(p))) 
    coin_hash = hashlib.sha256(bytes( p )).digest()
    #print(coin_hash[0:2])
    #print(list(coin_hash[:ONES]), looking_for)
    if list(coin_hash[0:ONES]) == looking_for:
        print("Found Coin")

    #print(hashlib.sha256(bytes(p )).hexdigest())




#s = '''0011001010000101011111010000101111111111101000001001000001001010110100010101111001001011000100111100011110001001111011110111011010010100110011001110111001100010111011010010101101010011110100100110101111110001100101011001000110100010000110110001100101110001'''
#h=int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
#a = binascii.hexlify(hashlib.sha256(h).digest()).decode()

#print(a[1])


