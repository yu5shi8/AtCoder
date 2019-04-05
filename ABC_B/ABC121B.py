# -*- coding: utf-8 -*-
# B - Can you solve this?
# https://atcoder.jp/contests/abc121/tasks/abc121_b

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = list()

for a_list in range(0, n):
    a_list = list(map(int, input().split())) 
    a.append(a_list)

count = 0
calc_n = 0
while calc_n < n:
    ab = 0
    calc_m = 0
    while calc_m < m:
        ab += a[calc_n][calc_m] * b[calc_m]
        calc_m += 1
    check = ab + c
    if check > 0:
        count += 1
    calc_n += 1
print(count)

# enumerate を選択肢に入れてみよう
# for i in range(n):
#     q = [a[i][j] * x for j, x in enumerate(b)]
#     if sum(q) + c > 0:
#         count += 1
# print(count)

