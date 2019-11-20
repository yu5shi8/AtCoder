# -*- coding: utf-8 -*-
# A - 宝くじ
# https://atcoder.jp/contests/arc006/tasks/arc006_1

E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))
cnt = 0

for i in range(6):
    if E[i] in L:
        cnt += 1

if cnt == 6:
    ans = 1
elif cnt == 5 and B in L:
    ans = 2
elif cnt == 5:
    ans = 3
elif cnt == 4:
    ans = 4
elif cnt == 3:
    ans = 5
else:
    ans = 0

print(ans)

# 18:15 - 18:26（AC）
