import numpy as np
import random


solution = ""

def get_solution():
    return solution

def create_matrix(w,h):
    Matrix = np.zeros((w,h), 'U1')
    Matrix.fill('G')

    for x in range(w):
        for y in range(h):
            Matrix[x][y] = random.choice('GDPR')

    return Matrix

def check_location(Matrix,w,h,x,y,xd,yd):
    if (xd>0 and (w-x)<4):
        return False
    if (xd<0 and x<4):
        return False
    if (yd>0 and (h-y)<4):
        return False
    if (yd<0 and y<4):
        return False
    return True


def check_direction(Matrix,x,y,xd,yd):
    return (Matrix[x][y]=='G' and Matrix[x+xd][y+yd]=='D' and Matrix[x+2*xd][y+2*yd]=='P' and Matrix[x+3*xd][y+3*yd]=='R')

def check_full_direction(Matrix,w,h,x,y,d,xd,yd):
    global solution
    if (check_location(Matrix,w,h,x,y,xd,yd) and check_direction(Matrix,x,y,xd,yd)) :
        solution = '[{2},{1},{0}]'.format(x+1,y+1,d)
        print solution
        return 1
    return 0

def count_matrix(Matrix,w,h):
    counter = 0
    for x in range(w-3):
        for y in range(h):
            counter += check_full_direction(Matrix,w,h,x,y,"d",1,0)
            counter += check_full_direction(Matrix,w,h,x,y,"dr",1,1)
            counter += check_full_direction(Matrix,w,h,x,y,"r",0,1)
            counter += check_full_direction(Matrix,w,h,x,y,"ur",-1,1)
            counter += check_full_direction(Matrix,w,h,x,y,"u",-1,0)
            counter += check_full_direction(Matrix,w,h,x,y,"ul",-1,-1)
            counter += check_full_direction(Matrix,w,h,x,y,"l",0,-1)
            counter += check_full_direction(Matrix,w,h,x,y,"dl",1,-1)
    return counter

def print_matrix(Matrix, counter):
    print counter
    for line in Matrix:
        print ' '.join(map(str, line))

def matrix_to_string(Matrix):
    stringy = []
    for line in Matrix:
        stringy.append(' '.join(map(str, line)))
    return '<br />\n'.join(map(str, stringy))

def create_and_print_matrix(w=4,h=4):
    print "Hello!"
    Matrix = create_matrix(w,h)
    counter = count_matrix(Matrix,w,h)
    print_matrix(Matrix, counter)
    print "Bye"

def create_checked_matrix(w=4,h=4):
    print "Hello!"

    Matrix = create_matrix(w,h)
    counter = count_matrix(Matrix,w,h)
    while (counter != 1) :
        Matrix = create_matrix(w,h)
        counter = count_matrix(Matrix,w,h)

    print_matrix(Matrix, counter)

    #print ''
    #print matrix_to_string(Matrix)
    print "Bye"
    return Matrix

#create_checked_matrix(10,10)

def test_matrix_module():
    Matrix = create_checked_matrix(10,10)
    print matrix_to_string(Matrix)
    print solution

if __name__ == "__main__":
    test_matrix_module()