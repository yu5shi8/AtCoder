# -*- coding: utf-8 -*-
# B - 町の合併
# https://atcoder.jp/contests/abc033/tasks/abc033_b

n = int(input())
sp = {}
all_member = 0
max_num = 0

for i in range(n):
    s, p = input().split()
    if s not in sp:
        sp.setdefault(s, int(p))
    else:
        sp[s] += int(p)
    all_member += int(p)
    if int(p) > max_num:
        max_num = int(p)

boss_city = [k for k, v in sp.items() if v == max_num]

if all_member // 2 < max_num:
    print('{}'.join(boss_city))
else:
    print('atcoder')

# 14:14 - 15:05（RE）
# 15:20（いったん離脱）
# 14:33 - 14:50（AC）
