#!/usr/bin/env python3

import sys

m, n, k, l = map(int, input().split())

matrix_mn = []
matrix_kl = []

for i in range(m):
    matrix_mn.append([x for x in map(int, input().split())])

for i in range(k):
    matrix_kl.append([x for x in map(int, input().split())])

if n != k:
    print('-1')
    sys.exit(0)

matrix_res = [[0]*l for i in range(m)]

for i in range(m):
    for j in range(l):
        sum = 0
        for k in range(n):
            sum += matrix_mn[i][k] * matrix_kl[k][j]
            # print(matrix_mn[i][k], '*', matrix_kl[k][j])
        # print('sum =', sum)
        matrix_res[i][j] = sum

for line in matrix_res:
    print(*line)
