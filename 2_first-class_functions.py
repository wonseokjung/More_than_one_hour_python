def factorial(n):
    """asdasd"""
    return 1 if n<1 else n*factorial(n-1)


print("factorial is " ,factorial(4))


print(factorial.__doc__)

fact = factorial

print(fact)

fruits= ['banana','strawberry','apple']

sort_fruits = sorted(fruits,key=len)
print(sort_fruits)

#reversing
def reverse(reverseword):
    return reverseword[::-1]

print(reverse("asdas"))


print(sorted(fruits,key =reverse))

a=list(map(fact,range(6)))

print(a)

b= [fact(n) for n in range(6)]

print(b)


c= list(map(fact, filter(lambda n: n%2,range(6))))

print(c)

from functools import reduce

from operator import add
d=reduce(add, range(100))

print(d)

e=sum(range(100))

print(e)


import random

class BingoCage:
    def __init__(self, items):
        self._items= list(items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo= BingoCage(range(3))

a=bingo.pick()

print(a)

a=dir(factorial)
print(a)
