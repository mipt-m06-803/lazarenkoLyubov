f=True

while f:
    n=int(input('введите число 0=exit : '))
    if n==0: break
    a= [i for i in range(n+1)]
    b=[]
    print (a)

    for i in range(2,n):
        if (i**2<=n) and (a[i]!=0):
            for j in range(i**2,n+1,i):
                a[j]=0
            #print(a)    
    for i in range(n+1):
        if a[i]!=0:
            b.append(a[i])              
    print(b)
