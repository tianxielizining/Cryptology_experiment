#! /usr/bin/env python
#! -^- coding = utf-8 -^-
# filename = mysha
# author = listennter
from Crypto.Hash import SHA

def mysha(text):
    mycrypt = SHA.new()
    mycrypt.update(text)
    return mycrypt.hexdigest()