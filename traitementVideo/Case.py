# -*- coding:utf-8 -*-

class Case:

    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return str(self.top_left) +" "+ str(self.top_right)+" "+str(self.bottom_left)+" "+ str(self.bottom_right)
