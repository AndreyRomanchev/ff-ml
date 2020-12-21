#!/usr/bin/env python3

n = int(input())
m = int(input())
k = int(input())

if k > n * m:
    print('NO')
elif k % n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')