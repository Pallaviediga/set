# 1.create a set with elements from 1 to 5. Add elements 6 to 7 to the set in one line.
s={1,2,3,4,5}
s.update({6,7})
print(s)

# output:
# {1,2,3,4,5,6,7}

# 2.Given two sets:Find elements that are present in A or B but not both(Symmetric difference)
A={1,2,3,4,5}
B={4,5,6,7,8}
res=A.symmetric_difference(B)
print(res)

# output:
# {1,2,3,6,7,8}

# 3.Remove an element from a set,but avoid error if element doesnot exist.Find maximum and minumum element from a 
s={5,8,12,3,15,7}
s.discard(9)
print(max(s))
print(min(s))

# output:
# max:15
# min:3

# 4.create a set with the values:10,20,30,40.then add the value 50 to the set.
s={10,20,30,40}
s.add(50)
print(s)

# output:
# {40,10,50,20,30}

# 5.Remove an elements 30 from a set {10,20,30,40,50}using a set method.
h={10,20,30,40,50}
h.remove(30)
print(h)

# output:
# {50,20,40,10}

# 6.Check whether the number 25 exists in the set{15,20,25,30,35}.
g={15,20,25,30,35}
print(25 in g)

# output:
# True

# 7.Find the union of two sets:
A={1,2,3,4}
B={3,4,5,6}
result=A.union(B)
print(result)

# output:
# {1,2,3,4,5,6}

# 8.Find the intersection of two sets:
A={10,20,30,40}
B={30,40,50,60}
res=A.intersection(B)
print(res)

# output:
# {40,30}
