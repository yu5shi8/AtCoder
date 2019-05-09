# -*- coding: utf-8 -*-
# B - 3人でカードゲームイージー / Card Game for Three (ABC Edit)
# https://atcoder.jp/contests/abc045/tasks/abc045_b

player = {}
player['a'] = input()
player['b'] = input()
player['c'] = input()

turn = 'a'
card = player[turn]

while card:
    head = card[0]
    player[turn] = player[turn][1:]
    turn = head
    card = player[turn]

print(turn.upper())

# 16:29 - 17:38
# （解答を閲覧）- 18:11
# 19:26 - 19:36
