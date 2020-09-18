# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:15:20 2020

@author: Asus
"""
from random import randint
from SnakeLadder1 import Board, GameMoves

num_snake = int(input('Enter number of snakes: '))
print('Enter the head and tail of the snakes in each line')
snake_pos = []
for i in range(num_snake):
    snake_pos.append(input())
    
num_ladder = int(input('Enter number of ladders: '))
print('Enter the bottom and top of ladder in each line')
ladder_pos = []
for j in range(num_ladder):
    ladder_pos.append(input())

num_players = int(input('Enter number of players: '))
print('Enter their names in each line')
player_names = []
positions = []
for k in range(num_players):
    player_names.append(input())
    positions.append(0)
    
board = Board(num_snake, snake_pos, num_ladder, ladder_pos)
snake_heads, snake_tails = board.snake()
ladder_bottom, ladder_top = board.ladder()

game = GameMoves(snake_heads, snake_tails, ladder_bottom, ladder_top)
count = 1
while 100 not in positions:
    print('Round', count, ':')
    for player in range(num_players):
        dice_value = randint(1, 6)
        print(player_names[player], 'moved from', positions[player], 'to', game.move(positions[player], dice_value))
        positions[player] = game.move(positions[player], dice_value)
    count += 1

print('Game finished -', player_names[positions.index(100)], 'has won')