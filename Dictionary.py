# Dictionary is a collection of keys-value pairs in Python.

"""
PROPERTIES OF PYTHON DICTIONARIES:

1. It is unordered. 
2. It is mutable. 
3. It is indexed. 
4. Cannot contain duplicate keys. 

"""

d = {} # Empty dictionary

marks = {
    "Akash": 100,
    "Shruti": 97,
    "Shubham": 56,
    "Rohan": 23,
    "marks":[92,98,96]
}


print(marks, type(marks))
print(marks["Shruti"])


# DICT METHODS :

marks1 = {
    "Akash": 100,
    "Shruti": 97,
    "Shubham": 56,
    "Rohan": 23,
    1: "Akash"
}

print(marks1.items())
print(marks1)

print(marks1.keys())
print(marks1)

print(marks1.values())
print(marks1)

marks1.update({"Akash": 99, "Rushu": 100})
print(marks1)

print(marks.get("Akash2")) # Prints None
# print(marks["Akash2"]) # Returns an error