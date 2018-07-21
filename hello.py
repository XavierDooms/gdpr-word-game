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

def count_matrix(carr,w,h):
    counter = 0
    for x in range(w-3):
        for y in range(h):
            if (carr[x][y]=='G' and carr[x+1][y]=='D' and carr[x+2][y]=='P' and carr[x+3][y]=='R') :
                print '[{0},{1}]'.format(x,y)
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


create_checked_matrix(10,10)


#@app.route('/')
#def index():   
#    return 'Index Page'

#@app.route('/hello')
#def hello():
#    return 'Hello, World'