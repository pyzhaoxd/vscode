a=[1,2,3]
b=[4,5,6]


for i,j in zip(a,b):
    with open('a.txt',mode='w') as f:
        f.write(i)