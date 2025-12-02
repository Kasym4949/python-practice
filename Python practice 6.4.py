nums=list(map(int,input("Enter the numbers: ").split()))
n=int(input("Choose a number from the list: "))
print(f"The number {n} appears {nums.count(n)} times in the list")
biggest=max(list)
smallest=min(list)
for i in set(list):
    print(f"{i} appears {nums.count(i)} times in the list")
print(f"The biggest number is: {biggest}, {nums.count(biggest)} times in the list")
print(f"The smallest number is: {smallest}, {nums.count(smallest)} times in the list")
even=[]
odd=[]
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"The even numbers are: {even}")
print(f"The odd numbers are: {odd}")
print(f"In ascending order: {sorted(nums)}")
print(f"In descending order: {sorted(nums, reverse=True)}")