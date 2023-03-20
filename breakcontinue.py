for x in range(3):
    print("x=" + str(x))
    if x == 1:
        break

for x in range(3, 0, -1):
    if x % 2 == 0:
        continue
    print(x)
