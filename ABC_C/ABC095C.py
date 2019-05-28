# -*- coding: utf-8 -*-
# C - Half and Half
# https://atcoder.jp/contests/abc095/tasks/arc096_a

a, b, c, x, y = map(int, input().split())

a_pizza = a * x
b_pizza = b * y
ans_1 = a_pizza + b_pizza

ans_2 = c * max(x, y) * 2

if x > y:
    ab_pizza_a = a * (x - y)
    ab_pizza_b = c * 2 * y
    ans_3 = ab_pizza_a + ab_pizza_b
else:
    ab_pizza_a = c * 2 * x
    ab_pizza_b = b * (y - x)
    ans_3 = ab_pizza_a + ab_pizza_b

print(min(ans_1, ans_2, ans_3))

# 17:20 - 22:14
