f=2*729**1021-2*243**1022+81**1023-2*27**1024-1025
t=0
print(f)
while f>0:
    if f % 3==0:
        t+=1
    f//=3
print(t)