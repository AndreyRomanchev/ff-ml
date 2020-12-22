#!/usr/bin/env python3

num_list = list(map(int, input().split()))

list_save = num_list.copy()

for i in range(1, len(num_list)):
    num_list[i] = list_save[i-1]

num_list[0] = list_save[-1]

print(' '.join(map(str, num_list)))