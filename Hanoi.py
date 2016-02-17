# -*- coding: utf-8 -*-
"""
利用递归移动汉诺塔
数量n的盘子借助c从a移动到b.
"""
count = 0

def mov(n, a, b, c):
    global count
    if n <= 0:
        return
    if n == 1:
        print("%s ==> %s" % (a, b))
        count += 1 
    else:
        mov(n-1, a, c, b)
        mov(1, a, b, c)
        mov(n-1, c, b, a)

mov(4, 'a', 'b', 'c')
print("Total steps: %s" % count)
