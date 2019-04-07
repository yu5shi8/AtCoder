# -*- coding: utf-8 -*-
# B - Five Dishes
# https://atcoder.jp/contests/abc123/tasks/abc123_b

'''
【解法わからず時間切れ】
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a, b, c, d, e]
order_l = []

for i in l:
  j = abs(123 - i)
  print(j)
  order_l.append(j)

ans = sum(l)
print(ans)
'''

# 解説を見て再回答
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

now_time = [a, b, c, d, e]
next_time = []

for i in now_time:
    if i % 10 == 0:
        next_time.append(i)
    else:
        while i % 10 != 0:
            i += 1
        next_time.append(i)

combined = sorted([x - y for (x, y) in zip(next_time, now_time)])

best_time = sum(next_time) - max(combined)
print(best_time)
