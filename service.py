#-^- coding = utf-8 -^-
#author = listennter
from flask import Flask
from flask import request
from flask import make_response,Response
import json


from lab1 import *
from lab2 import *
from lab4 import *
from lab5 import *

app = Flask(__name__)

def setlog(text,name):
    with open(name,'w') as f:
	#f.write('\n-------writing log-------\n')
	f.write(text)	
@app.route('/')    
def hello():
    return 'Hello World!'

#lab1
@app.route('/gcd',methods=['POST'])
def test_number():
    a = request.form.get('first')
    b = request.form.get('second')
    a = int(a,10)
    b = int(b,10)
    result = str(gcd(a,b))
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/inverse',methods=['POST'])
def element_inverse():
    a = request.form.get('first')
    b = request.form.get('second')
    a = int(a,10)
    b = int(b,10)
    result = e_inverse(a,b)
    if result == -1:
        result = 'There is no Inverse element!'
    else: 
        result = str(result)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/sqare_mod',methods=['POST'])
def Modulus_squared_residue():
    num = request.form.get('first')
    sqr = request.form.get('second')
    m   = request.form.get('third')
    num = int(num,10)
    sqr = int(sqr,10)
    m   = int(m,10)
    result = str(ax_mod_m(num,sqr,m))
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

# lab2
@app.route('/affine_encode',methods=['POST'])
def encry_affine():
    express = request.form.get('first')
    key1 = request.form.get('second')
    key2 = request.form.get('third')
    k = int(key1,10)
    b = int(key2,10)
    result = affine_encode(express,k,b)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/affine_decode',methods=['POST'])
def decry_affine():
    cipher = request.form.get('first')
    key1 = request.form.get('second')
    key2 = request.form.get('third')
    k = int(key1,10)
    b = int(key2,10)
    result = affine_decode(cipher,k,b)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

#lab4
@app.route('/des_encode',methods=['POST'])
def des_encode():
    form_code = request.form.get('first')
    key       = request.form.get('second')
    result = desencode(form_code,key)
    setlog(result)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/des_decode',methods=['POST'])
def des_decode():
    key_code = request.form.get('first')
    key      = request.form.get('second')
    result = desdecode(key_code,key)
    print result
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/aes_encode',methods=['POST'])
def aes_encode():
    text = request.form.get('first')
    key  = request.form.get('second')
    mycrypt = MyAES(key)
    result = mycrypt.myencrypt(text)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/aes_decode',methods=['POST'])
def aes_decode():
    text = request.form.get('first')
    key  = request.form.get('second')
    mycrypt = MyAES(key)
    result = mycrypt.mydecrypt(text)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp
@app.route('/rsa_encode',methods=['POST'])
def _rsa_encode():
    message = request.form.get('second')
    key     = request.form.get('first')
    head = '-----BEGIN PUBLIC KEY-----'
    tail = '-----END PUBLIC KEY-----'
    real_key = ''
    for i in key:
	if i == '\x20':
		real_key += '\x0a'
	else:
		real_key += i
    real_key = head + real_key[26:-24] + tail
    #real_key = real_key[:-1]
    setlog(real_key,'my_public.pem')
    with open('my_public.pem') as f:
	real_key = f.read()
    	result  = RSAencode(message.encode('ascii'),real_key)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/rsa_decode',methods=['POST'])
def _rsa_decode():
    message = request.form.get('first')
    key     = request.form.get('second')
    random  = request.form.get('third')
    head = '-----BEGIN PRIVATE KEY-----'
    tail = '-----END PRIVATE KEY-----'
    real_key = ''
    for i in key:
	if i == '\x20':
		real_key += '\x0a'
	else:
		real_key += i
    real_key = head + real_key[27:-25] + tail
    #real_key = real_key[:-1]
    setlog(real_key,'my_private.pem')
    setlog(random,'my_random')
    with open('my_private.pem') as f:
	real_key = f.read()
	with open('my_random') as ran:
		random = ran.read()
    		result  = RSAdecode(message.encode('ascii'),real_key,random)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp


# lab5`
@app.route('/sha-1',methods=['POST'])
def sha_1():
    text = request.form.get('first')
    result = mysha(text)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/rsa_sign',methods=['POST'])
def _rsa_sign():
    message = request.form.get('first')
    key     = request.form.get('second')
    head = '-----BEGIN PRIVATE KEY-----'
    tail = '-----END PRIVATE KEY-----'
    real_key = ''
    for i in key:
	if i == '\x20':
		real_key += '\x0a'
	else:
		real_key += i
    real_key = head + real_key[27:-25] + tail
    #real_key = real_key[:-1]
    setlog(real_key,'my_private.pem')
    with open('my_private.pem') as f:
	real_key = f.read()
    	result = rsa_sign(message.encode('ascii'),real_key)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp

@app.route('/rsa_verify',methods=['POST'])
def _rsa_verify():
    message = request.form.get('first')
    key     = request.form.get('third')
    sign    = request.form.get('second')
    head = '-----BEGIN PUBLIC KEY-----'
    tail = '-----END PUBLIC KEY-----'
    real_key = ''
    for i in key:
	if i == '\x20':
		real_key += '\x0a'
	else:
		real_key += i
    real_key = head + real_key[26:-24] + tail
    #real_key = real_key[:-1]
    setlog(real_key,'my_public.pem')
    with open('my_public.pem') as f:
	real_key = f.read()
    	result  = rsa_verify(message.encode('ascii'),sign.encode('ascii'),real_key)
    esp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print resp
    return resp


if __name__ == '__main__':
    app.run('0.0.0.0',1234,True)
