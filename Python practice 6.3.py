nums=list(map(int,input("The list: ").split()))
n=int(input("Choose a number from the list: "))
a=nums.count(n)
print(f"The number {n} appears {a} times in the list.")