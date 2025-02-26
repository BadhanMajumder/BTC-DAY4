def prim(n,m):
    if(n==0 or m==1):
        n=2
    s=range(n,m)
    for i in s:
        for num in range(2,i):
        
            if(i%num==0):
                break
        
        else:
                print(f"{i} is a prime number")

a=int (input("Enter the num : "))
b=int (input("Enter the num : "))
prim(a,b)