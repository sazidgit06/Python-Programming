name = "!!!!!Sazid!!!!!!"
print(name.rstrip("!"))
print(name.lstrip("!"))
print(name.upper())
print(name.lower())
print(name.replace("Sazid", "hasan"))

str1 = "Welcome to python programming 09 A to Z"
print(str1.endswith("to", 0, 10))
print(name.endswith("!"))
print(name.startswith("!"))

print(str1.find("python"))
print(str1.find("pythonframework"))

print(str1.index("python"))
#print(str1.index("pythonprogramming")) # This will raise a ValueError

str2 = "HelloWorld"
str3 = "HelloWorld123"

print(str3.isalnum())
print(str2.isalpha())

print(str.islower())
print(str.isupper())

print(str.isprintable())
print(str.istitle())
print(str.swapcase())
print(str.title())