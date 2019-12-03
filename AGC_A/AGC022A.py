# -*- coding: utf-8 -*-
# A - Diverse Word
# https://atcoder.jp/contests/agc022/tasks/agc022_a

S = input()

for i in range(ord('a'), ord('z')+1):
    if chr(i) not in S:
        print(S + chr(i))
        exit()
else:
    for i in range(len(S)-1, -1, -1):
        for j in range(ord('a'), ord('z')+1):
            if S[i] < chr(j) and chr(j) not in S[:i]:
                print(S[:i] + chr(j))
                exit()
    else:
        print(-1)

# [1] 15:16 - 15:58（WA）- 16:06（解説・解答を閲覧）
# [2] 16:31 - 16:51（AC）
