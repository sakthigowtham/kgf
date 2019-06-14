m1=int(input());
o=0
if(m1==2 or m1==3):
  print("yes")
else:
  for i in range(2,m1):
    if(m1%i==0):
      o=0
      print("no")
      break
    else:
     o=1
     continue  
  if(o!=0):
    print("yes");
