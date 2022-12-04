#%%Part A
bags = open('code/day03_puzzleinput.txt','r').read().split('\n')
print(bags)
wiki='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

c=[]
for bag in bags:
    comp1 = bag[0:int(len(bag)/2)]
    comp2 = bag[int(len(bag)/2):]#
    for item in comp1:
        if item in comp2:
            c.append(wiki.index(item)+1)
            break

print(sum(c))




#%%PART B
c2=[]
for i in range(len(bags)//3):
    bagset = (bags[i*3],bags[i*3+1],bags[i*3+2])
    poss_badges=[]
    for item in bagset[0]:
        if item in bagset[1] and item in bagset[2]:
            c2.append(wiki.index(item)+1)
            break

print(sum(c2))