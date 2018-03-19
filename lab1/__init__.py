#! usr/env/bin python
#-^- coding = utf-8 -^-
#author = listennter

def gcd(num1,num2):
    if num2 == 0:
        return num1
    if num1 < num2:
        return gcd(num2,num1)
    else:
        return gcd(num2,num1%num2)

def fenjie(n):
    for i in xrange(2, n+1):
        counter = 0
        while n % i == 0:
            n /= i
            counter += 1
        if counter:
            yield (i, counter)

def euler(n):
    assert n > 0
    counter = 1
    for a, x in fenjie(n):
       counter *= (a-1) * (a**(x-1)) 
    return counter
    
def ax_mod_m(a, x, m):
    assert a > 0 and x >= 0
    if x == 0:
        return 1
    return ax_mod_m(a, x/2, m) ** 2 * a ** (x&1) % m

def e_inverse(n, m):
    if gcd(n,m) == 1:
        return ax_mod_m(n, euler(m)-1, m)
    else:
        return -1
