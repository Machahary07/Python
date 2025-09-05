#WAF that accepts a list of integers and returns two values, the sum of odd & even numbers.
def sumofoddeven(l):
    o=0
    e=0
    for n in l:
        if n%2==0:
            e+=n
        else:
            o+=n
    return o,e

o,e=sumofoddeven([1,2,3,4,5,6,7,8,9])
print("Sum of odd numbers:",o,"Sum of even numbers:",e)
