#! /usr/bin/env python
import random
import time
x = 0
while x < 5:
    y = random.randrange(0, 10)
    if y == 7:
        print ('lucky 7')
        x += 1
    if y == 5:
        print ('that was a five')
        x += 1
    print ('Hi spam')
    x += 1
    time.sleep(y/100)
print ('done')
