#!/usr/bin/env python3

num_list = list(map(int, input().split()))

count_dict = {}
max = 0
maxi = 0

for i in num_list:
    if i not in count_dict:
        count_dict[i] = 0
    count_dict[i] += 1
    if count_dict[i] > max:
        max = count_dict[i]
        maxi = i
    elif count_dict[i] == max and i > maxi:
        maxi = i

print(maxi)
