# -*- coding: utf-8 -*-
# C - Dubious Document 2
# https://atcoder.jp/contests/abc076/tasks/abc076_c

S = input()[::-1]
T = input()[::-1]

for i in range(len(S)-len(T)+1):
    for j in range(len(T)):
        if T[j] != S[i+j] != '?':
            break
    else:
        break
else:
    print('UNRESTORABLE')
    exit()

ans = (S[:i] + T + S[i+len(T):])[::-1]
ans = ans.replace('?', 'a')
print(ans)

# [1] 13:53 - 14:41（WA）/ 13:26 - 13:49（WA / 解説・解答を閲覧）14:03
# [2] 15:09 - 15:27（解答を閲覧）
# [3] 15:35 - 15:43（WA / 解答を閲覧）
# [4] 16:07 - 16:11（AC）
