# given an input contains MxN matrix with 0 & 1s. 0s indicating black pixel and 1 indicating white pixel and output as getting all the coordinates of the start and end for all the possible boxes of patches formed by the group of 1's

def startandend(i,j,a,op,pos):
    x = len(a)
    y = len(a[0])
    fc = 0
    fr = 0
    for k in range(i,x):
        if a[k][j] == 0:
            fr = 1 
            break
        if a[k][j] == 5:
            pass
        for n in range(j, y):
            if a[k][n] == 0:
                fc = 1 
                break
            a[k][n] = 5
    if fr == 1:
        op[pos].append( k-1)
    else:
        op[pos].append(k)
    if fc == 1:
        op[pos].append(n-1)
    else:
        op[pos].append
def finalwhitepatches(a):
    s= len(a)
    op = []
    pos = -1
    for i in range(0,s):
        for j in range(0, len(a[0])):
            if a[i][j] == 1:
                op.append([i, j])
                pos+= 1       
                startandend(i, j, a, op, pos)
    print (op)
inputcase= [
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
finalwhitepatches(inputcase)
# output for above inputcase is [[0, 1, 1, 5], [3, 1, 4, 5]]
