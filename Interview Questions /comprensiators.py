# comprehensions - comprensiators are  1 4 types
# what is comprehension? - it is a way to create a new sequence from an existing sequence in a single line  1 code
#  list comprehension
sqr = [x+2+(x**2) for x in range(10)if x%2==0]
print("sqr :",sqr)

count = [x for x in range(1,21)]
print("count :",count)
# set comprehension
s = {x**2 for x in range(10) if x%2==0}
print("set s :",s)
# --> set s : {0, 64, 4, 36, 16}
# dictionary comprehension
d = {x:x**2 for x in range(10) if x%2==0}
print("dict d :",d)
# generator comprehension
g = (x**2 for x in range(10) if x%2==0)
print("generator g :",list(g))
print("type of g :",type(g))
print("next  1 g :",next(g))
print("next  2 g :",next(g))
print("next  3 g :",next(g))
print("next  4 g :",next(g)) 
