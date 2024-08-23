def greet(name):
    print(f"Hello! {name}\n")

def Arithmetic(a,b):
    print(f"Sum of {a} and {b} = {a+b}")
    print(f"Sub of {a} and {b} = {a-b}")
    print(f"Multiplication of {a} and {b} = {a*b}")
    print(f"Division of {a} and {b} = {a/b}")
    print(f"Exponential of {a} and {b} = {a**b}")
    print(f"Floor Division of {a} and {b} = {a//b}")

def multiplicationTable(n):
    print(f"\n===== Multiplication Table of {n}===========")
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

greet("Shruti")
Arithmetic(2,3)
multiplicationTable(5)