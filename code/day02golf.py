s='B XC YA ZA XB YC ZC XA YB Z13232121213'
print(sum([(s.index(i[0:3])/3+1) for i in open('code/2.txt')]) , sum([(int(s[int(s.index(i[0:3])/3)+27])+int(s.index(i[2])-2)) for i in open('code/2.txt')]))