# -*- coding: utf-8 -*-
# B - 価格の合計
# https://atcoder.jp/contests/abc014/tasks/abc014_2

n, X = map(int, input().split())
a = list(map(int, input().split()))
a.reverse()
ans = 0

bin_x = format(X, 'b')
bin_x = bin_x.zfill(n)

for i in range(n):
    if bin_x[i] == '1':
        ans += a[i]

print(ans)

# 9:13 - 9:44（AC）
