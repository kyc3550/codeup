# https://codeup.kr/problem.php?id=4816


n = int(input())
a=0
b=0
c=0

if n/10 != 0:
    print(-1)
    break

if n>=300:
    while (n>=300):
        n = n % 300
        a=a+1
if n>=60:       
    while (n>=60):
        n = n % 60
        b=b+1

if n<60:
    c = n/10
    
print(a,b,int(c))
