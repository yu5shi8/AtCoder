# -*- coding: utf-8 -*-
# B - Trick or Treat
# https://atcoder.jp/contests/abc166/tasks/abc166_b

N, K = map(int, input().split())
ans = [None] * N

for _ in range(K):
    D = int(input())
    A = list(map(int, input().split()))
    for d in range(D):
        if ans[A[d]-1] == None:
            ans[A[d]-1] = True

print(ans.count(None))

# 18:04 - 18:16（AC）
