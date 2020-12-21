#!/usr/bin/env python3

s = 777

for i in range(10):
   s += 40
   s -= s * 7 // 100

print(s)