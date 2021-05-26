# https://codeup.kr/problem.php?id=1165&rid=0

a,b = map(int,input().split(' '))
while True:
  if a>=90:
    break
  else:
    a=a+5
    b=b+1
print(b)
