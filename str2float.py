# -*- coding: utf-8 -*-

from functools import reduce

def fn(ss):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[ss]

def str2float(s):
    pos = s.find('.')
    ss = s.replace('.','')

    result = reduce(lambda x, y: x*10 +y, map(fn,ss))
    #return result
    print 10**(len(s)-(1 + pos))
    return result*1.0/(10**(len(s)-(1 + pos)))

print('str2float(\'123.456\') =', str2float('123.456'))
