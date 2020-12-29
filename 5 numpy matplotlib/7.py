#!/usr/bin/env python3


def transpose(matrix: list) -> list:
    nl = len(matrix)
    ml = len(matrix[0])

    res = [[0] * nl for i in range(ml)]

    for i in range(ml):
        for j in range(nl):
            res[i][j] = matrix[j][i]

    return res

n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append([x for x in map(int, input().split())])

for line in transpose(matrix):
    print(*line)

