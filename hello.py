from flask import Flask
import numpy as np
import random
app = Flask(__name__)

solution = ""

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

def check_full_direction(Matrix,w,h,x,y,xd,yd):
    if (check_location(Matrix,w,h,x,y,xd,yd) and check_direction(Matrix,x,y,xd,yd)) :
        solution = '[d,{1},{0}]'.format(x+1,y+1)
        print solution
        counter = counter + 1

def count_matrix(Matrix,w,h):
    counter = 0
    for x in range(w-3):
        for y in range(h):
            if ((w-x)>=4 and check_direction(Matrix,x,y,1,0)) :
                print '[d,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((w-x)>=4 and (h-y)>=4 and check_direction(Matrix,x,y,1,1)) :
                print '[dr,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((h-y)>=4 and check_direction(Matrix,x,y,0,1)) :
                print '[r,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and (h-y)>=4 and check_direction(Matrix,x,y,-1,1)) :
                print '[ur,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and check_direction(Matrix,x,y,-1,0)) :
                print '[u,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (x>=4 and y>=4 and check_direction(Matrix,x,y,-1,-1)) :
                print '[ul,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if (y>=4 and check_direction(Matrix,x,y,0,-1)) :
                print '[l,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
            if ((w-x)>=4 and y>=4 and check_direction(Matrix,x,y,1,-1)) :
                print '[dl,{0},{1}]'.format(x+1,y+1)
                counter = counter + 1
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


@app.route('/')
def index():
    html_string = "<html>\n"
    html_string += "<head><style>body { font-family: Courier; }</style></head>\n"
    html_string += "<body>\n"
    html_string += "<h1>Find \"GDPR\"</h1>\n"
    html_string += "<div>\n"
    html_string += matrix_to_string(create_checked_matrix(10,10))
    html_string += "</div>\n"
    html_string += "<div hidden>\n"
    html_string += "Location: {}\n".format(solution)
    html_string += "</div>\n"
    html_string += "\n</body>\n</html>"

    return html_string

@app.route('/hello')
def hello():
    return 'Hello, World'