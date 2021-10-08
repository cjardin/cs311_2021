import hashlib
from itertools import product
import binascii

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool #uses processors



#problem space = all possible search points 
jobs_to_do = []

def min_coin(x):
    repeat = x['repeat'] #how man bytes
    mod_number = x['mod_number'] #how man processers to run
    mod_pos = x['mod_pos'] # which processor am I
    ones = x['ones'] # the number of ones to search for

    looking_for = [1] * ones
    count=0
    perm = product(list(range(256)), repeat=repeat)
    coins_found = []
    for p in perm:
        #print(p)
        if (count % mod_number) == mod_pos:
            coin_hash = hashlib.sha256(bytes( p )).digest()
            if list(coin_hash[0:ones]) == looking_for:
                coins_found.append(p)

    return coins_found




jobs_to_do.append( {'repeat' :2, 'mod_number': 2, 'mod_pos': 1, 'ones': 2} ) 
jobs_to_do.append( {'repeat' :2, 'mod_number': 2, 'mod_pos': 0, 'ones': 2} )
jobs_to_do.append( {'repeat' :2, 'mod_number': 2, 'mod_pos': 1, 'ones': 1} )
jobs_to_do.append( {'repeat' :2, 'mod_number': 2, 'mod_pos': 0, 'ones': 1} )

jobs_to_do.append( {'repeat' :3, 'mod_number': 2, 'mod_pos': 1, 'ones': 2} )
jobs_to_do.append( {'repeat' :3, 'mod_number': 2, 'mod_pos': 0, 'ones': 2} )
jobs_to_do.append( {'repeat' :3, 'mod_number': 2, 'mod_pos': 1, 'ones': 1} )
jobs_to_do.append( {'repeat' :3, 'mod_number': 2, 'mod_pos': 0, 'ones': 1} )



#with ThreadPoolExecutor(max_workers=2) as exe:
#     result = exe.map(min_coin ,jobs_to_do)
with Pool(8) as p: 
    print(p.map(min_coin, jobs_to_do))

#here p does NOT exist



