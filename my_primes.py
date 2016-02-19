# -*- coding: utf-8 -*-
'''
生成素数的集合
'''

def odd_set(n = 3):
    while True:
        yield n
        n = n + 2

def filter_sushu( L , l):
    def func(n):
        if n % l > 0:
            return True
        return False
    LL = filter(func , L)
    return LL

def primes():
    yield 2
    it = odd_set()
    while True:
        l =  next(it)
        it =  filter_sushu(it, l)
        yield l

num = primes()
for i in range(10):
    print(next(num))
