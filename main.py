# Simple Python program for Google App Engine testing

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Google App Engine Python Test")
print("-----------------------------")

x = 10
y = 5

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))

for i in range(1, 6):
    print("Number:", i)