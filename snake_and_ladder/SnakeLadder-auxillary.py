# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:49:32 2020

@author: Asus
"""

class Board:
    def __init__(self, num_snake, pos_snake, num_ladder, pos_ladder):
        self.num_snake = num_snake
        self.pos_snake = pos_snake
        self.num_ladder = num_ladder
        self.pos_ladder = pos_ladder
        self.snake_head = []
        self.snake_tail = []
        self.ladder_bottom = []
        self.ladder_top = []
        
    def snake(self):
        for i in range(self.num_snake):
            temp = self.pos_snake[i].split(' ')
            self.snake_head.append(int(temp[0]))
            self.snake_tail.append(int(temp[1]))
        return self.snake_head, self.snake_tail
    
    def ladder(self):
        for i in range(self.num_ladder):
            temp = self.pos_ladder[i].split(' ')
            self.ladder_bottom.append(int(temp[0]))
            self.ladder_top.append(int(temp[1]))
        return self.ladder_bottom, self.ladder_top
    
class GameMoves:
    def __init__(self, snake_head, snake_tail, ladder_bottom, ladder_top):
        self.snake_head = snake_head
        self.snake_tail = snake_tail
        self.ladder_bottom = ladder_bottom
        self.ladder_top = ladder_top
    
    def move(self, present_pos, dice_value):
        next_pos = present_pos + dice_value
        
        if next_pos in self.snake_head:
            idx = self.snake_head.index(next_pos)
            next_pos = self.snake_tail[idx]
            return next_pos
        
        elif next_pos in self.ladder_bottom:
            idx = self.ladder_bottom.index(next_pos)
            next_pos = self.ladder_top[idx]
            return next_pos
        
        elif next_pos>100:
            return present_pos
        
        else:
            return next_pos