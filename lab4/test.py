#! _*_ coding = utf-8 _*_
from my_RSA import RSAdecode,RSAencode
from DES import *

if __name__ == '__main__':
	with open('my_public.pem') as f:
		key = f.read()
		message = 'helloyky'
		result = RSAencode(message,key)
	print result
