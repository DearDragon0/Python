# Example of break in a for loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Example of continue in a while loop
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)

# Example of a while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Increment the count to eventually make the condition false

# Example of a for loop iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of a for loop using range()
for i in range(5):  # This will iterate from 0 to 4
    print(i)
