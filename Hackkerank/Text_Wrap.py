# Q: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    n = len(string)
    for i in range(0,n):
        print(string[i], end ="")
        i +=1
        if i !=0 and i%max_width == 0:
            print('')
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
