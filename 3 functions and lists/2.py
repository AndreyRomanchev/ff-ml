#!/usr/bin/env python3

num_list = list(map(int, input().split()))

for i in range(0, len(num_list) // 2 * 2, 2):
    num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

print(' '.join(map(str, num_list)))