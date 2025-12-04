numbers = list(map(int, input("Enter numbers: ").split()))
info = {}

for num in set(numbers):
    info[num] = {"count": numbers.count(num), "indexes": []}

for index, value in enumerate(numbers):
    info[value]["indexes"].append(index)

for value in sorted(info):
    print(f"{value}: appears {info[value]['count']} times, indexes = {info[value]['indexes']}")