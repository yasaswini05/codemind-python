x=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(x-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c