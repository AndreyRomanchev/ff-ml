#!/usr/bin/env python3

x = float(input())
y = float(input())
x_c = float(input())
y_c = float(input())
r = float(input())


def is_point_in_circle(x:float, y:float, x_c:float, y_c:float, r:float) -> bool:
    return (x-x_c)**2 + (y-y_c)**2 <= r*r


if is_point_in_circle(x, y, x_c, y_c, r):
    print('YES')
else:
    print('NO')