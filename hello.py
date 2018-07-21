#from flask import Flask
import numpy as np
import random
#app = Flask(__name__)


def create_matrix(w,h):
    carr = np.zeros((w,h), 'U1')
    carr.fill('G')

    for x in range(w):
        for y in range(h):
            carr[x][y] = random.choice('GDPR')
    
    return carr

def check_direction(carr,x,y,xd,yd):
    return (carr[x][y]=='G' and carr[x+xd][y+yd]=='D' and carr[x+2*xd][y+2*yd]=='P' and carr[x+3*xd][y+3*yd]=='R')

def count_matrix(carr,w,h):
    counter = 0
    for x in range(w-3):
        for y in range(h):
            if ((w-x)>=4 and check_direction(carr,x,y,1,0)) :
                print '[d,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((w-x)>=4 and (h-y)>=4 and check_direction(carr,x,y,1,1)) :
                print '[dr,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((h-y)>=4 and check_direction(carr,x,y,0,1)) :
                print '[r,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and (h-y)>=4 and check_direction(carr,x,y,-1,1)) :
                print '[ur,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and check_direction(carr,x,y,-1,0)) :
                print '[u,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and y>=4 and check_direction(carr,x,y,-1,-1)) :
                print '[ul,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (y>=4 and check_direction(carr,x,y,0,-1)) :
                print '[l,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((w-x)>=4 and y>=4 and check_direction(carr,x,y,1,-1)) :
                print '[dl,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
    return counter

def print_matrix(carr, counter):
    print counter
    for line in carr:
        print ' '.join(map(str, line))

def create_and_print_validated_matrix(w=4,h=4):
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

    print "Bye"
    return Matrix


create_checked_matrix(10,10)


#@app.route('/')
#def index():   
#    return 'Index Page'

#@app.route('/hello')
#def hello():
#    return 'Hello, World'