# WAP to find the sum of even numbers from 1 to n.

input = int(input("Enter a number: "))
sum = 0
for i in range(1, input+1):
    if i% 2 ==0:
        sum += i
print("Sum of even numbers from 1 to", input, "is", sum)
