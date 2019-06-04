# -*- coding: utf-8 -*-
# A - 高橋君と青木君の好きな数
# https://atcoder.jp/contests/abc032/tasks/abc032_a

a = int(input())
b = int(input())
n = int(input())
num = n

while n <= num:
    if num % a == 0 and num % b == 0:
        ans = num
        break
    else:
        num += 1

print(ans)

# 21:38 - 21:43
