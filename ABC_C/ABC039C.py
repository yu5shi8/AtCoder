# -*- coding: utf-8 -*-
# C - ピアニスト高橋君
# https://atcoder.jp/contests/abc039/tasks/abc039_c

S = input()
kb = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW'
scale = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si']

for i in range(12):
    if S[0:] == kb[i:i+20]:
        ans = scale[i]
        break

print(ans)

# 13:31 - 13:46（AC）
