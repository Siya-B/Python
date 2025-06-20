fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)
    
    print()

for fruit in fruits:
    if fruit == "cherry":
       pass
    print(fruit)
    
#while loop

count = 0

while count< 5:
    print(count)
    count += 1
    if count == 3:
        break