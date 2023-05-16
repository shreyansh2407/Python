a = {1,4,5,5,5,2,3,4}

#set is well defined collection of elements which are distinct
print(a)
# print(a.clear)
a.pop()         #pop any random element
print(a)

b = {2,6,8,5,7,10}

print(a.union(b)) #return set containing union of both sets
print(a.intersection(b)) #return set containing intersection of both sets
print(a)
print(b)
