n=int(input())
x=0
for i in range(n):
    oper=input()
    if "--" in oper:
        x=x-1
    elif "++" in oper:
        x=x+1
print(x)
