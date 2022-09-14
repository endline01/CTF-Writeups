#!/usr/bin/python3
from string import printable
from pwn import xor
cipher = open('cipher.enc','rb').read()
key = 'perfect'
flag = b''
for char in printable:
	x = xor(cipher,key+char).decode()
	if 'yuctf{X' in x and '}' in x[-1]:
		print(x);break
print(cipher)
