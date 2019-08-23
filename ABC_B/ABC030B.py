# -*- coding: utf-8 -*-
# B - 時計盤
# https://atcoder.jp/contests/abc030/tasks/abc030_b

n, m = map(int, input().split())

if n > 12:
    n -= 12
n += m / 60

n_deg = 30 * n
m_deg = 6 * m

ans = abs(n_deg - m_deg)
print(min(ans, abs(360 - ans)))

# [1] 21:45 - 22:32（WA）- 22:45（AC）
# [2] 15:11 - 15:16（WJ -> WA）- 17:30（AC）
