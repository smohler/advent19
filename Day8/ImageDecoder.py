# Load Image Data
import numpy as np
import math
Data = list(open('input.txt', 'r').read().strip()) #row = 6, col = 25
example = [0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0] # row = 2, col = 2
#Black:Positive, White:Negative, Trans:Zero
data = Data
row, col = 6, 25
ValueMap = {0:1, 1:-1, 2:0}

image = list(map(int, data))
imageVisibilityValues  = list(map(lambda x: ValueMap[x], image))
size = row*col
number_of_layers = range(int(len(image)/size))
#make each layer a matrix of visibility values (row = 6, col = 25)
Layers = [np.array(imageVisibilityValues[i*size:i*size + size]).reshape((row,col)) \
for i in number_of_layers]

ViewableImage = Layers[0]*0
k = 1
for Layer in reversed(Layers):
    ViewableImage = ViewableImage + math.factorial(k)*Layer
    k = k+1
#Every time a layer is added a pixel value p is now either 
# p>0:Black, p<0:White, or p=0:Transparent because of the factorial scale every addition override the previous

Color = lambda x: ' ' if x>0 else 'X'
PrintImage = [Color(ViewableImage[i][j]) for i in range(row) for j in range(col)]

#Print Result in Terminal (could just use a package to make an image)
for i in range(row):
    for j in range(col):
        if j == col-1:
            print(str(PrintImage[col*i+j]))
        else:
            print(str(PrintImage[col*i+j]), end = " ")