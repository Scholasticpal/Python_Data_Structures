f1 = 0
f2 = 1
num = 0
i = 1
n = int(input("Enter number of values needed"))
print(f1)
print(f2)
while i+1 < n:
    num = f1 + f2
    f1 = f2
    f2 = num
    print(num)
    num = 0
    i = i+1
