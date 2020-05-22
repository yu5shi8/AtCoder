# -*- coding: utf-8 -*-
# C - Guess The Number
# https://atcoder.jp/contests/abc157/tasks/abc157_c

N, M = map(int, input().split())
ans = ['-1'] * N

if N == 1 and M == 0:
    print(0)
    exit()

for i in range(M):
    s, c = map(int, input().split())
    if ans[s-1] == str(c):
        continue
    elif ans[s-1] == '-1':
        ans[s-1] = str(c)
    else:
        print(-1)
        exit()

if N >= 2 and ans[0] == '0':
    print(-1)
    exit()
elif ans[0] == '-1':
    ans[0] = '1'

ans = ''.join(ans).replace('-1', '0')
print(ans)

# [1] 16:19 - 16:35（RE）- 16:40（WA）- 16:42（WA）- 16:51（WA）- 17:02（WA）- 17:05（他解答を参照してAC）
