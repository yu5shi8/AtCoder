# -*- coding: utf-8 -*-
# B - Five Dishes
# https://atcoder.jp/contests/abc123/tasks/abc123_b

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
l = [a, b, c, d, e]
sur = [0] * 5

for i in range(len(l)):
    if l[i] % 10 != 0:
        sur[i] = 10 - (l[i]%10)

ans = sum(l) + sum(sur) - max(sur)
print(ans)

# 18:19 - 19:00（RE / WA）
# - 19:08（WA）
# （解答を閲覧）- 19:20
