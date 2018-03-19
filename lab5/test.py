#! /usr/bin/env python
#! _*_ coding = utf-8 _*_

from rsa_sign import rsa_sign,rsa_verify

if __name__ == '__main__':
    '''
    with open('my_private.pem') as f:
        key = f.read()
        message = raw_input('input:')
        print rsa_sign(message,key)
        '''
    with open('my_public.pem') as f:
        key = f.read()
        message = raw_input('input message:')
        sign = raw_input('input sign:')
        print rsa_verify(message,sign,key)