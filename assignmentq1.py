x = int(input("Enter the value of x"))
n = int(input("Enter the range till which you want the values to be print"))
sum = 0
for i in range(1, n+1):
    val = x ** (-i)
    sum = sum + val

print("The value for the given sigma operation is", sum)

