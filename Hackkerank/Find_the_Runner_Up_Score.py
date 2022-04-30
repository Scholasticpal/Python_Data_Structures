# Q: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

#better soln: print(sorted(list(set(arr)))[-2])
if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())

  list =[]
  for val in arr: 
    if val in list: 
     continue 
    else:
      list.append(val)
  res = sorted(list)
  print (res[-2])
