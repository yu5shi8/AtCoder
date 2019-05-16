# -*- coding: utf-8 -*-
# B - *e**** ********e* *e****e* ****e**
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b

n = int(input())
s = input()
k = int(input())

temp = s[k-1]
ans = s.replace(temp, '0')

for i in ans:
    if i != '0':
        ans = ans.replace(i, '*')

print(ans.replace('0',temp))
