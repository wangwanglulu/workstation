#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# 牌组：2-10 直接用数值表示，J、Q、K 作为 10，A 作为 11（可以调整为 1）
def create_deck():
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 
    deck = values * 4  # 4种花色
    random.shuffle(deck)
    return deck

# 计算手牌点数（考虑 A=11 变 A=1 的情况）
def calculate(cards):
    total = sum(cards)
    aces = cards.count(11)
    while total > 21 and aces > 0:
        total -= 10  # 将 A 从 11 变 1
        aces -= 1
    return total

def player_turn(player_hand, deck):
    while True:
        score = calculate(player_hand)  # 直接调用计算函数
        print(f"玩家手牌: {player_hand}，当前点数: {score}")
        if score >= 21:
            break
        move = input("是否要牌？(y/n): ")
        if move == 'y':
            player_hand.append(deck.pop())
        else:
            break
    return score, deck  # 直接返回计算出的分数

def dealer_turn(dealer_hand, deck):
    while calculate(dealer_hand) < 17:  # 只要小于 17 就继续要牌
        dealer_hand.append(deck.pop())
    return calculate(dealer_hand), deck  

def blackjack():
    deck = create_deck()
    # 发两张初始手牌
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    # 玩家回合
    player_score, deck = player_turn(player_hand, deck)
    if player_score > 21:
        print("玩家爆牌，庄家获胜！")
        return
    # 庄家回合
    dealer_score, deck = dealer_turn(dealer_hand, deck)
    print(f"庄家手牌: {dealer_hand}，点数: {dealer_score}")
    # 判定胜负
    if dealer_score > 21 or player_score > dealer_score:
        print("玩家获胜！")
    elif player_score == dealer_score:
        print("平局！")
    else:
        print("庄家获胜！")
blackjack()



