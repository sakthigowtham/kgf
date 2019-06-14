s=int(input());
e=list(map(int,input().strip().split()))[:s]
e.sort();
print(" ".join(str(a) for a in e));
