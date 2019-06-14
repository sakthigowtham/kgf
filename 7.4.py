def add(a,b):
    p=a+b
    return p
N,M=input().split()
N=int(N);
M=int(M);
a=add(N,M)
if(a%2==0):
    print("even")
else:
    print("odd");
