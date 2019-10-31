# -*- coding: utf-8 -*-
# A - 鉛筆リサイクルの新技術
# https://atcoder.jp/contests/arc011/tasks/arc011_1

m, n, N = map(int, input().split())
stock = N
ans = N

while stock // m > 0:
    r_num, r_mod = divmod(stock, m)
    r_sale = r_num * n
    ans += r_sale
    stock = r_sale + r_mod

print(ans)

# 17:03 - 17:22（AC）
