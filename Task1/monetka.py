# Примитивный эмулятор броска монетки n раз

import random

def monetka(n):
    for i in range(n):
        m = random.randint(1,2)
        if m == 1:
            print("орел")
        else:
            print("решка")


n = int(input())
monetka(n)