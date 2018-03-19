#! /usr/bin/env python
#! _*_ coding = utf-8 _*_ 
# filename = my_RSA.py
# author = listennter
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

def RSAencode(message,key):
    rsaKey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsaKey)
    cipher_text = base64.b64encode(cipher.encrypt(message))
    return cipher_text

def RSAdecode(message,key,random):
    rsaKey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsaKey)
    text = cipher.decrypt(base64.b64decode(message),random)
    return text 