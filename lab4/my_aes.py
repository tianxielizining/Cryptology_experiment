#! /use/bin/env python
#! -^- coding = utf-8 -^-
# filename = my_aes
# author = listennter
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex

class MyAES():
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC
    
    def myencrypt(self,text):
        length = 16
        count = len(text)
        #print count 
        if count < length :
            add = length - count 
            text += '\0'*add
        elif count > length :
            add = length - (count%length)
            text += '\0'*add
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def mydecrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
