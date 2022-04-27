
MAX = 100000
x = int(input("Enter Number: "))
n = int(input("Enter power of number: "))
def multiply(x, res, res_size):
    # Initialize carry
    carry = 0

    # One by one multiply n with
    # individual digits of res[]
    for i in range(res_size):
        prod = res[i] * x + carry
        res[i] = prod % 10
        carry = prod // 10

    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1
    return res_size

def power(x, n):
    # printing value "1" for power = 0
    if (n == 0):
        print("1")
        return


res = [0 for i in range(MAX)]
res_size = 0
temp = int(x)

# Initialize result
while (temp != 0):
    res[res_size] = temp % 10
    res_size += 1
    temp = temp // 10

# Multiply x n times
# (x^n = x*x*x....n times)
for i in range(2, n + 1):
    res_size = multiply(x, res, res_size)

print(x, "^", n, " = ", end="")
for i in range(res_size - 1, -1, -1):
    print(res[i], end="")

# Driver program

exponent = 100
base = 2
power(base, exponent)
