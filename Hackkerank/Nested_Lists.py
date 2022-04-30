# Q: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

res =[]
scorelist = []

if __name__ == '__main__':

    for _ in range(int(input())):
        name = input()
        score = float(input())
        res +=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(res):
        if c==b:
            print(a)
