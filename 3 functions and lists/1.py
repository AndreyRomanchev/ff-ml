#!/usr/bin/env python3

num_list = list(map(int, input().split()))

res = 0

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        # print(i, j)
        if num_list[i] == num_list[j]:
            # print('i', i, 'j', j)
            res += 1

print(res)
