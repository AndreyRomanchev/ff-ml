#!/usr/bin/env python3

s = input()

num = []

result = 0

for l in s:
    if l.isdigit():
        num.append(int(l))
    else:
        if num:
            for i, digit in enumerate(num[::-1]):
                result += digit * (10 ** i)
            num = []

if num:
    for i, digit in enumerate(num[::-1]):
        result += digit * (10 ** i)

print(result)
