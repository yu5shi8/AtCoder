# -*- coding: utf-8 -*-
# B - Bounding
# https://atcoder.jp/contests/abc130/tasks/abc130_b

n, x = map(int, input().split())
l = list(map(int, input().split()))

bound = [0]
ans = 1

for i in range(n):
    bound.append(bound[i] + l[i])
    ans += 1
    if bound[-1] == x:
        break
    elif bound[-1] > x:
        ans -= 1
        break

print(ans)

# 21:02 - 21:12
