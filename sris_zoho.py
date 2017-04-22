n=int(input("Enter the number:"))
ls=[]
cout=0
for i in range(2,n):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=flag+1
            break
    if(flag==0):
        ls.append(i)
for i in ls:
    for j in ls:
        if(cout==1):
            break
        a=i+j
        if(a==n):
            cout=cout+1
            a=i
            b=j
if(cout!=0):
    print("%d+%d=%d"%(a,b,n))
    print(True)
else:
    print(False)

            
