l = [11, 45, 1, 2, 4, 6, 1, 1]
l.append(7)
print(l)
# l.sort(reverse=True)
# l.reverse()
print(l.index(1))  # This method returns the index of the first occurrence of the list item.
# print(l.count(1))  # count the occurrences of given number
# m = l.copy()  # to make copy (m = l will refrence the m to l so change in m will be change in l )
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
# l.extend(m)
print(l)