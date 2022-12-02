#%%PART A
data = open('day1_puzzleinput.txt','r')
datalist= data.read().split('\n\n')

clist = []
for item in datalist:
    itemlist = item.split('\n')
    sumlist = []
    for it in itemlist:
        it = int(it)
        sumlist.append(it)
    cal = sum(sumlist)
    clist.append(cal)

clist.sort()
print(clist[-1])

#%%PART B
print(sum(clist[-3:]))

