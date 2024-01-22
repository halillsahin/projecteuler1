üçebölünenler=[]
beşebölünenler=[]
onbeşebölünenler=[]
for i in range(1,1000):
    if i%3==0:
        üçebölünenler.append(i)
for i in range(1,1000):
    if i%5==0:
        beşebölünenler.append(i)
for i in range(1,1000):
    if i%15==0:
        onbeşebölünenler.append(i)
a=sum(üçebölünenler)
b=sum(beşebölünenler)
c=sum(onbeşebölünenler)
print(a+b-c)        