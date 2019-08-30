# -*- coding: utf-8 -*-
# C - Not so Diverse
# https://atcoder.jp/contests/abc081/tasks/arc086_a

n, k = map(int, input().split())
a = list(map(int, input().split()))

num = len(set(a))
ans = 0

if num <= k:
    print(ans)
    exit()
else:
    dict_a = {}
    for i in a:
        if i not in dict_a:
            dict_a[i] = 1
        else:
            dict_a[i] += 1
    a_values = [v for v in dict_a.values()]
    a_values.sort()
    i = 0
    while num > k:
        ans += a_values[i]
        num -= 1
        i += 1

print(ans)

# 11:02 - 11:29（AC）
