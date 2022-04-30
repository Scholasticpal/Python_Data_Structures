# Q: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    lis = []
    for i in range(0,N):
        req = input().split()
        
        if req[0] == "print":
            print(lis)
        elif req[0] == "insert":
            lis.insert(int(req[1]), int(req[2]))
        elif req[0] == "append":
            lis.append(int(req[1]))
        elif req[0] == "sort":
            lis.sort()
        elif req[0] == "remove":
            lis.remove(int(req[1]))
        elif req[0] == "pop":
            lis.pop()
        elif req[0] == "reverse":
            lis.reverse()
