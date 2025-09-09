#WAF that takes an int n & returns the factorial of n & the number of digits in that factorial
def fact():
    n = int(input("Enter a number: "))
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f, len(str(f))
print(fact())