# Q: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0.00
    for i in student_marks:
        if i == query_name:
            for i in student_marks[i]:
                sum += i
    avg = sum/3.00
    result = "{:.2f}".format(avg)
    print(result)
