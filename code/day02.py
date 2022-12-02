#%%PART A
wiki={'A':1,'X':1,'B':2,'Y':2,'C':3,'Z':3}
points={-1:6,2:6,0:3,1:0,-2:0}

games = [(item.strip()) for item in open('code/day02_puzzleinput.txt').readlines() ]
pts=[]
for game in games:
    plays = game.split(' ')
    pts.append(points[wiki[plays[0]]-wiki[plays[1]]] + wiki[plays[1]])
print(sum(pts))




#%%PART B
import numpy as np
cmd = {'X':[1,-2],'Y':[0,0],'Z':[-1,2]}

pp = []
for game in games:
    plays =  game.split(' ')
    arr = np.array(sorted([(wiki[plays[0]] - item) for item in cmd[plays[1]]]))
    yourplay = arr[(arr >= 1) & (arr <= 3)][0] #nice way to remove all upper and lower values arr[(arr >= lower) & (arr <= upper)] instead of np.clip()
    pp.append(yourplay + points[cmd[plays[1]][0]])
print(sum(pp))




