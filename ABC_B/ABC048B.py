# -*- coding: utf-8 -*-
# B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b

a, b, x = map(int, input().split())

def calc(n):
    if n >= 0:
        num = n // x + 1
    else:
        num = 0
    return num

ans = calc(b) - calc(a-1)
print(ans)

'''
for i in range(10**18):
    print(i*x)
    if a <= i*x <= b:
        count += 1
    elif b < i*x:
        print(count)
        exit()
print(count)

# オーバーフローするから、アプローチを変えないといけない…
'''

# 10:58 - 11:25
# （解説を閲覧）- 11:32
