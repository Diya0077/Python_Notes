# Set is a collection of well-defined, non-repetitive objects/elements. 

'''
PROPERTIES OF SETS: 

1. Sets are unordered => Element’s order doesn’t matter 
2. Sets are unindexed => Cannot access elements by index 
3. There is no way to change items in sets. 
4. Sets cannot contain duplicate values. 

'''

e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 


print(s)


# SET METHODS


s = {1, 5, 32, 54,5, 5, 5, "AKASH"}

print(s, type(s))

s.add(566)
print(s)
s.remove(1)
print(s)


# UNION & INTERSECTION:

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))