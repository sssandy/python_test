# -*- coding: utf-8 -*-
#!/usr/bin/env python
 
def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
 
if __name__ == "__main__":
    g = pas_triangles()
    #for n in range(10):
    #    print(next(g)) 
    print(next(g))
