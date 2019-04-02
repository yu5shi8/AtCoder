# -*- coding: utf-8 -*-
# A - Sandglass2
# https://atcoder.jp/contests/abc072/tasks/abc072_a

x, t = map(int, input().split())
ans = x - t
if ans > 0:
    print(ans)
else:
    print(0)

# max()を使えば、0かansのうち、数値の大きな方をスマートに返せる
