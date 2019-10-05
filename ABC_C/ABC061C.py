# -*- coding: utf-8 -*-
# C - Big Array
# https://atcoder.jp/contests/abc061/tasks/abc061_c

N, K = map(int, input().split())
st = {}

for i in range(N):
    a, b = map(int, input().split())
    st[a] = st.get(a, 0)
    st[a] += b

st_sorted = sorted(st.items(), key=lambda x:x[0])

num = 0
for i in range(len(st_sorted)):
    num += st_sorted[i][1]
    if num >= K:
        print(st_sorted[i][0])
        exit()

# 16:00 - 16:05（WA）- 16:39（AC）
