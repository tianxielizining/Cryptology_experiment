#! /usr/env/bin python
#-^- coding = utf-8 -^-
#author = listennter
from lab1 import e_inverse,gcd

letter_length = 26
def affine_encode(express,k,b):
    result = ''
    if gcd(k,letter_length) != 1:
        return 'The key is not safe!'
    for c in express:
        if c.isalpha():
            c_encode = ((ord(c) - ord('a')) * k + b) % letter_length
            result += chr(c_encode + ord('a'))
        else:
            result += c
    return result

def affine_decode(cipher,k,b):
    result = ''
    yek = e_inverse(k,letter_length)
    if  gcd(k,letter_length) != 1:
        return 'The cipher CAN NOT be decipher!'
    for c in cipher:
        if c.isalpha():
            c_decode = yek*(ord(c) - ord('a') - b) % letter_length
            result += chr(c_decode + ord('a'))
        else:
            result += c
    return result