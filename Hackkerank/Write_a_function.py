# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    if(year%4 == 0):
        if(year%100 == 0):
            if(year%400 == 0):
                leap = True
            else: break
            else: break
    # Write your logic here

    return leap

year = int(raw_input())
print is_leap(year)