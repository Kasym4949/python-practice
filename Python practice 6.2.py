e=[]
o=[]
n=int(input("Enter the number: "))
for i in range(1,n+1):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(f"The even numbers are: {e}")
print(f"The odd numbers are: {o}")