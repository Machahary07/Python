# WAF that takes length and breadth of a rectangle & returns its perimeter and area
def rect(l, b):
    a = l * b
    p = 2 * (l + b)
    return a, p

a, p = rect(2, 3)
print("Area:", a, "Perimeter:", p)