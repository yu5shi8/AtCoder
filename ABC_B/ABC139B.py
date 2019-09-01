# -*- coding: utf-8 -*-
# B - Power Socket
# https://atcoder.jp/contests/abc139/tasks/abc139_b

A, B = map(int, input().split())
ans = 0
socket = 1

while socket < B:
    socket += (A - 1)
    ans += 1

print(ans)

# 21:03 - 21:04（WA）- 21:38（WA）- 22:16（WA）- （解説を閲覧）22:47 -（解答を閲覧）22:52
