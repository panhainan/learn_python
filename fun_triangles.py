# -*- coding: utf-8 -*-
#!/usr/bin/env python
 
def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
 
