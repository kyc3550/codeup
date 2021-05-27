#https://codeup.kr/problem.php?id=2001

pasta = []
juice = []

for p in range(3):
    pasta.append(int(input()))

for j in range(2):
    juice.append(int(input()))


answer = min(pasta)+min(juice)
print(round(answer*1.1,1))
