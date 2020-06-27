# -*- coding: utf-8 -*-
# C - One Quadrillion and One Dalmatians
# https://atcoder.jp/contests/abc171/tasks/abc171_c

N = int(input())
name = []
alphabet = [chr(i) for i in range(97, 97+26)]

while 0 < N:
    num = N // 26
    mod = N % 26
    if 26 < num:
        if mod == 0:
            name += alphabet[-1]
            num -= 1
        else:
            name += alphabet[mod-1]
    else:
        if mod == 0:
            name += alphabet[-1]
            num -= 1
        else:
            name += alphabet[mod-1]
    N = num

name.reverse()
print(*name, sep='')

# 21:05 - 21:51（AC）
