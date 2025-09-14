sum=0
for i in range(20):
    if i % 2 == 0:
        continue
    if i==15:
        break
    sum += i
    print(i)
print(sum)