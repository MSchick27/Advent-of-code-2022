import numpy as np
mes4=4
mes=14

data = open('code/day06_puzzleinput.txt').read()

for i in range(len(data)-3):
    quad = list(data[i:i+mes])
    arr = np.array([quad])
    if len(np.unique(arr)) == mes:
        print(i+mes)
        break