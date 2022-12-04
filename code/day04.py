#%%PART A and B
import numpy as np
jobs = open('code/day04_puzzleinput.txt','r').read().split('\n')

a,b=0,0
for pair in jobs:
    job = pair.split(',')
    job1 = job[0].split('-')
    job2 = job[1].split('-')
    job1 = np.arange(int(job1[0]),int(job1[1])+1,1)
    job2 = np.arange(int(job2[0]),int(job2[1])+1,1)
    if set(job1).issubset(set(job2)) == True:
        a = a+1
    elif set(job2).issubset(set(job1)) == True:
        a = a+1
    if bool(set(job1) & set(job2)) == True:
        b=b+1
print(a,b)

