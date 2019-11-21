# -*- coding: utf-8 -*-
# A - お買い物クライシス
# https://atcoder.jp/contests/arc019/tasks/arc019_1

S = input()
change = {'O':'0', 'D':'0', 'I':'1', 'Z':'2', 'S':'5', 'B':'8'}
ans = ''

for s in S:
    if s in change:
        ans += change[s]
    else:
        ans += s

print(ans)

# 11:34 - 11:41（AC）
