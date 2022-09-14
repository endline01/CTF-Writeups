#!/usr/bin/python3
from Crypto.Cipher import DES
from base64 import *
from Crypto.Util.number import long_to_bytes

c=0x8c5f0e4dbf1ba3293d71a147294f10e89b75e635122ffc1b #from the output
ciphertext=long_to_bytes(c)
KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

#using this writeup and edit the script https://noob-atbash.github.io/CTF-writeups/cyberwar/crypto/chal-5
#yuctf{W34k_3ncrypt10n}
