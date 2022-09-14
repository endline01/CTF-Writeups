import hashlib
from random import shuffle  , randint
f=open('wordlist.txt','rb').readlines()


shuffle(f)

word = f[randint(0 , len(f))].decode().strip('\n')

def enc(w):
	r = ''
	for i in w[::-1]:
		r+= hashlib.sha256(hashlib.md5(i.encode()).hexdigest().encode()).hexdigest()
	return r

print('c = ' , enc('???')+enc(word)[3:]) 
