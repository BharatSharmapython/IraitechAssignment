# 2, 3, 10, 15, 26, 35, 50, 63, ?

for i in range(1, 10):
    if (i % 2) == 0:
        val = (i * i) - 1
        print(val, " ", end="")
    else:
        val = (i * i) + 1
        print(val, " ", end="")

