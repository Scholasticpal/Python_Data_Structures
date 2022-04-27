#Factorial of a number
n = int(input("Enter number to get factorial: "))
f = n
while(n!=1):
    f = f * n-1
    n = n-1

print("factorial: ", f)
