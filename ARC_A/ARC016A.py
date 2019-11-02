# -*- coding: utf-8 -*-
# A - クイズゲーム
# https://atcoder.jp/contests/arc016/tasks/arc016_1

N, M = map(int, input().split())

ans = [i for i in range(1, N+1)]
ans.pop(M-1)

print(ans[0])

# 16:39 - 16:41（AC）
