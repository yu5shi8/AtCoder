# -*- coding: utf-8 -*-
# D - Friends
# https://atcoder.jp/contests/abc177/tasks/abc177_d

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n + 1)
        self.rank=[0] * (n + 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y

            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def size(self, x):
        return -self.parents[self.find(x)]

N, M = map(int, input().split())

uf = UnionFind(N)
ans = 0

for m in range(M):
    A, B = map(int, input().split())
    uf.union(A, B)

for n in range(1, N+1):
    ans = max(ans, uf.size(n))

print(ans)

# 21:40 - 21:59（WA）
# 18:45 - 19:34（解答を写経）- 19:41（AC）
