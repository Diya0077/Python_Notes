"""
# For Reading from a File

f = open("MyHubby.txt")
# sen = f.readline() #Reads a single Line
# sen = f.readlines() # Reads the strings and return a list
sen = f.read()
print(sen)
f.close()

"""
# For Writing in a file
# str = "I love you"
# f = open("Love.txt","w")
# sen = f.write(str)
# f.close()

# For Appending in a File
str1 = "I love you\n"
f = open("Love.txt","a")
f.write(str1)  
f.close()