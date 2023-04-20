l = [1, 2, 3, 4, 5, 6]

# functions who takes function as argument are called higher order functions

# MAP
# newl = []
# for i in l:
    # newl.append(lambda x: x*x*x)

mapl = list(map(lambda x: x*x*x, l))

print(mapl)

# FILTER
filterl = list(filter(lambda a: a<4, l))

print(filterl)

from functools import reduce

# calculates the sum of the numbers using the reduce function
sum = reduce(lambda a, b: a+b, l)
# works like this in above case
# [1, 2, 3, 4, 5, 6] -> [1+2, 3, 4, 5, 6] -> [3+3, 4, 5, 6] -> and so on

print(sum)
