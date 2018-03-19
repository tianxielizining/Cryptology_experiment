#! /usr/bin/env python
#! _*_ coding = utf-8 _*_
# filename = Create_RSA_key.py
# author = listennter

from Crypto import Random
from Crypto.PublicKey import RSA

# Random generator
my_random = Random.new().read
# Generating RSA instance
my_rsa = RSA.generate(1024,my_random)

#print my_random
with open('my_random.pem','w') as f:
    f.write(str(my_random))

# read the created private key
private_pem = my_rsa.exportKey()
# out put the key
with open('my_private.pem','w') as f:
    f.write(private_pem)
public_pem = my_rsa.publickey().exportKey()
with open('my_public.pem','w') as f:
    f.write(public_pem)

