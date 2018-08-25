def rotateImage(a):
    x = 0
    n = len(a)
    while(x < int(len(a)/2)):
        y = x
        while(y < len(a)-1-x):
                temp = a[y][x]
                a[y][x] = a[n-1-x][y]
                a[n-1-x][y] = a[n-1-y][n-1-x]
                a[n-1-y][n-1-x] = a[x][n-1-y]
                a[x][n-1-y] = temp
                y += 1
        x += 1
        
    return a