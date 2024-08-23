# Parameterised Function
def avg(a, b):
    return (a+b)/2


# Non-Parameterised Function
def greet():
    print("Good Morning!")


# Function with default arguments
def greet1(name, ending="Thank You"):
    print(f"Hii! {name}")
    print(ending)


# In order to use the function we need to call it

greet()
c = avg(5,6)
print(c)
# greet1("Shruti")
greet1("Shruti", "Thanks") #ending when passes will take precedence over the default argument