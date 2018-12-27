import numpy as np
import random

class WordPuzzle:
    def __init__(self,width=10,height=10,word="GDPR"):
        self.width = width
        self.height = height
        self.word = word
        self.solution = ""

        self.direction_dict = {
            'down':(1,0),
            "down-right":(1,1),
            "right":(0,1),
            "up-right":(-1,1),
            "up":(-1,0),
            "up-left":(-1,-1),
            "left":(0,-1),
            "down-left":(1,-1)}

        self.create_checked_puzzle()

    def check_direction(self,position,direction):
        for step in range(len(self.word)):
            x_test = position[0]+step*direction[0]
            y_test = position[1]+step*direction[1]
            if (self.Matrix[x_test][y_test] != self.word[step]):
                return False
        return True

    def direction_within_borders(self,position,direction):
        word_len = len(self.word)
        if (direction[0]>0 and (self.width-position[0])<word_len):
            return False
        if (direction[0]<0 and position[0]<word_len):
            return False
        if (direction[1]>0 and (self.height-position[1])<word_len):
            return False
        if (direction[1]<0 and position[1]<word_len):
            return False
        return True

    def direction_has_solution(self,position,direction):
        if (not self.direction_within_borders(position,self.direction_dict[direction]) or
            not self.check_direction(position,self.direction_dict[direction])):
            return 0

        self.solution = '[{2},{1},{0}]'.format(position[0]+1,position[1]+1,direction)
        print(self.solution)
        return 1

    def has_only_one_solution(self):
        counter = 0
        for x in range(self.width):
            for y in range(self.height):
                counter += self.direction_has_solution((x,y),"down")
                counter += self.direction_has_solution((x,y),"down-right")
                counter += self.direction_has_solution((x,y),"right")
                counter += self.direction_has_solution((x,y),"up-right")
                counter += self.direction_has_solution((x,y),"up")
                counter += self.direction_has_solution((x,y),"up-left")
                counter += self.direction_has_solution((x,y),"left")
                counter += self.direction_has_solution((x,y),"down-left")
                if (counter>1):
                    return False
        return (counter == 1)

    def set_new_random_puzzle(self):
        Matrix = np.zeros((self.width,self.height), 'U1')
        Matrix.fill('G')
        for x in range(self.width):
            for y in range(self.height):
                Matrix[x][y] = random.choice(self.word)
        self.Matrix = Matrix

    def create_checked_puzzle(self):
        self.set_new_random_puzzle()
        while(not self.has_only_one_solution()):
            self.set_new_random_puzzle()

    def html_string(self):
        stringy = []
        for line in self.Matrix:
            stringy.append(' '.join(map(str, line)))
        return '<br />\n'.join(map(str, stringy))

def test_puzzle_module():
    puzzle = WordPuzzle(20,20,"OLIFANT")
    print(puzzle.html_string())
    print(puzzle.solution)

if __name__ == "__main__":
    test_puzzle_module()