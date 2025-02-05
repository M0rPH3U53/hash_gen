#!/usr/bin/python3

import time
from hashlib import *

from blake3 import blake3

print(
    """

  /$$$$$$                      /$$   /$$                     /$$      
 /$$__  $$                    | $$  | $$                    | $$      
| $$  \__/  /$$$$$$  /$$$$$$$ | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$ 
| $$ /$$$$ /$$__  $$| $$__  $$| $$$$$$$$ |____  $$ /$$_____/| $$__  $$
| $$|_  $$| $$$$$$$$| $$  \ $$| $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$
| $$  \ $$| $$_____/| $$  | $$| $$  | $$ /$$__  $$ \____  $$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
 \______/  \_______/|__/  |__/|__/  |__/ \_______/|_______/ |__/  |__/

by M0rPH3U53                                                              
"""
)
txt = input("Entrez votre texte: ")

print("\n" "Hash (Sécurité forte) :" "\n")

# SHA-512
print("SHA512: -->", sha512(txt.encode()).hexdigest())

# SHA3-512
print("SHA3-512: -->", sha3_512(txt.encode()).hexdigest())

# Blake2b
print("Blake2b: -->", blake2b(txt.encode()).hexdigest())

# Blake2s
print("Blake2s: -->", blake2s(txt.encode()).hexdigest())

# Blake3
print("Blake3: -->", blake3(txt.encode()).hexdigest())

# Shake-128
print("SHAKE-128: -->", shake_128(txt.encode()).hexdigest(65))

# Shake-256
print("SHAKE-256: -->", shake_256(txt.encode()).hexdigest(65))

print("\n" "Hash (Sécurité faible) :" "\n")

# MD5
print("MD5: -->", md5(txt.encode()).hexdigest())

# SHA-1
print("SHA-1: -->", sha1(txt.encode()).hexdigest())

# SHA-224
print("SHA-224: -->", sha224(txt.encode()).hexdigest())

# SHA-256
print("SHA-256: -->", sha256(txt.encode()).hexdigest())

# SHA-384
print("SHA-384: -->", sha384(txt.encode()).hexdigest())

# SHA3-224
print("SHA3-224: -->", sha3_224(txt.encode()).hexdigest())

# SHA3-256
print("SHA3-256: -->", sha3_256(txt.encode()).hexdigest())

time.sleep(500)
