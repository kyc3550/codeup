#https://codeup.kr/problem.php?id=3301

n = int(input())

money = [50000,10000,5000,1000,500,100,50,10]
cnt = 0

for b in money:
    cnt = cnt + n//b
    n = n % b
    
print(cnt)
