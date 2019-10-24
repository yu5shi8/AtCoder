# -*- coding: utf-8 -*-
# A - Dividing a String
# https://atcoder.jp/contests/agc037/tasks/agc037_a

S = input()

check = S[0]
now = ''
cnt = 1

for i in range(1, len(S)):
    now += S[i]
    if check != now:
        check = now
        now = ''
        cnt += 1

print(cnt)

# [1] 14:47 - 16:02（WA）
# [2] 16:08 - 16:10（AC）
