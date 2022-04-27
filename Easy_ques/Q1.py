# given a list iterate it and display numbers which are divisible by 5
# if you find number greater than 150 stop the iteration

li = [12, 15, 32, 42, 55, 75, 122, 132, 150, 200]
for i in li:
    if i <= 150 and i % 5 == 0:
        print(i)
