# -*- coding: utf-8 -*-
# A - お茶
# https://atcoder.jp/contests/abc036/tasks/abc036_a

a, b = map(int, input().split())

if b % a != 0:
    ans = b // a + 1
else:
    ans = b // a

print(ans)



# 20:14 - 20:16
