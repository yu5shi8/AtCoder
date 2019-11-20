# -*- coding: utf-8 -*-
# A - くつがくっつく
# https://atcoder.jp/contests/arc024/tasks/arc024_1

L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = 0

l.sort()
r.sort()

if L >= R:
    for i in range(L):
        if l[i] in r:
            ans += 1
            r.pop(r.index(l[i]))
else:
    for i in range(R):
        if r[i] in l:
            ans += 1
            l.pop(l.index(r[i]))

print(ans)

# 17:36 - 17:41（WA）- 18:04（AC）
