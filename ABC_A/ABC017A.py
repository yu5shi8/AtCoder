# -*- coding: utf-8 -*-
# A - プロコン
# https://atcoder.jp/contests/abc017/tasks/abc017_1

se = [list(map(int, input().split())) for _ in range(3)]
ans = 0

for i in se:
    ans += int(i[0] * (i[1]*0.1))

print(ans)

# 10:21 - 10:28
