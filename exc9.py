n = int(input('insert size of array: '))
a = list(range(n))

#a=list(input('insert list'))
#for i in len(a):
#    a[i]=int(a[i])
s = int(input('input max summ: '))
d = 0
print(a)
b = len(a)
print(b)
for i in range(b):
    for j in range(i+1,b):
       # print(i,j,sum(a[i:j+1]))
        if sum(a[i:j+1])>s:
            d+=1
            print(i,j)
print(d)
            