# -*- coding: utf-8 -*-
# B - Judge Status Summary
# https://atcoder.jp/contests/abc173/tasks/abc173_b

N = int(input())
ans = [0] * 4

for s in range(N):
    s = input()
    if s == 'AC':
        ans[0] += 1
    elif s == 'WA':
        ans[1] += 1
    elif s == 'TLE':
        ans[2] += 1
    else:
        ans[3] += 1

print('AC x ' + str(ans[0]))
print('WA x ' + str(ans[1]))
print('TLE x '+ str(ans[2]))
print('RE x ' + str(ans[3]))

# 16:35 - 16:39（AC）
