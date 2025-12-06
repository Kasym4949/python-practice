n=int(input("Number of people: "))
people = {}

for _ in range(n):
    name=input("Name: ")
    age=int(input("Age: "))
    people[name]=age
print("\nFull dict:", people)

min_age=min(people.values())
max_age=max(people.values())

print(f"\nThe youngest age: {min_age}")
print(f"The oldest age: {max_age}")

sorted_names=sorted(people.keys())
print("\nNames (Alphabetically):", sorted_names)

adults={name: age for name, age in people.items() if age >= 18}
print("\n18+ people:", adults)
print("\nElements (enumerate):")

for index, (name, age) in enumerate(people.items()):
    print(f"{index}: Name = {name}, Age = {age}")