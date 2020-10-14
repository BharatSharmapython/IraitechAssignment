x = int(input("Enter the value of x"))
y = int(input("Enter the value of y"))
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

val = (((x + (1/y)) ** a) * ((x - (1/y)) ** b)) / (((y + (1/x)) ** a) * ((y - (1/x)) ** b))
print(val)
