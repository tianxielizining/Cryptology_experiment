#! /usr/bin/env python
#!_*_ coding = utf-8 _*_
# filename = rsa_sign.py
# author = listennter

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.Hash import SHA
import base64

def rsa_sign(message,key):
    rsaKey = RSA.importKey(key)
    signer = Signature_pkcs1_v1_5.new(rsaKey)
    digest = SHA.new()
    digest.update(message)
    sign  = signer.sign(digest)
    signature = base64.b64encode(sign)
    return signature

def rsa_verify(message,sign,key):
    rsaKey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsaKey)
    digest = SHA.new()
    digest.update(message)
    is_verify = verifier.verify(digest,base64.b64decode(sign))
    return is_verify