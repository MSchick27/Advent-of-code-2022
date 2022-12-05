import numpy as np


data = open('code/day05_puzzleinput.txt')

data = data.read().split('\n\n')
boxes = data[0].split('\n')
cmds = data[1].split('\n')

indexlist=[]
numbers = boxes[-1].strip()
numbers=numbers.replace(' ','')
    

chests=[]

for vbox in boxes:
    for i in range(len(numbers)):
        i = 1 + i*4
        chests.append(vbox[i])

chests = chests[:-len(numbers)]

arr = np.array(chests)
arr = np.reshape(arr,(len(boxes)-1, len(numbers)))
print(arr)
arr =np.rot90(arr,k=3, axes=(0,-1))

fbox = []
for c in range(len(arr[0])+1):
    fbox.append(list(arr[c]))   #lists?

ffbox = []
for l in fbox:
    for item in l:
        if ' ' in l:
            l.remove(' ')
        if ' ' in l:
            l.remove(' ')
        
    ffbox.append(l)

for com in cmds:
    com= com.split(' ')
    num = int(com[1])
    x0 =int(com[3])-1
    x1 = int(com[5])-1
    
    b = ffbox[x0][:-num]
    c =ffbox[x0][::-1]
    
    a =ffbox[x1]
    for item in c[:num]:
        a.append(item)
    ffbox[x0]=b
    ffbox[x1]=a

    #print(ffbox)

result=[]
for lists in ffbox:
    result.append(lists[-1])


e = ''.join(result)
print(e)




#%%PArt B

ffbox = []
for l in fbox:
    for item in l:
        if ' ' in l:
            l.remove(' ')
        if ' ' in l:
            l.remove(' ')
        
    ffbox.append(l)


for com in cmds:
    com= com.split(' ')
    num = int(com[1])
    x0 =int(com[3])-1
    x1 = int(com[5])-1
    
    b = ffbox[x0][:-num]
    c =ffbox[x0]        #changes for PART B
    
    a =ffbox[x1]
    for item in c[-num:]:   #changes for PART B
        a.append(item)
    ffbox[x0]=b
    ffbox[x1]=a

    #print(ffbox)

result=[]
for lists in ffbox:
    result.append(lists[-1])


e = ''.join(result)
print(e)