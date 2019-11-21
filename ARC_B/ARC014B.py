# -*- coding: utf-8 -*-
# B - あの日したしりとりの結果を僕達はまだ知らない。
# https://atcoder.jp/contests/arc014/tasks/arc014_2

N = int(input())
play = ['LOSE', 'WIN']
l = []

for i in range(N):
    w = input()
    num = i % 2
    if w in l:
        print(play[num])
        exit()
    if i >= 1:
        prev = l[-1][-1]
        check = w[0]
        if prev != check:
            print(play[num])
            exit()
    l.append(w)

print('DRAW')

# 11:07 - 11:23（AC）
