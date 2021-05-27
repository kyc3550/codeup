tcal = []

n = int(input())

a,b = map(int,input().split(' '))

dcal = int(input())

for i in range(n):
    tcal.append(int(input()))

tcal.sort(reverse=True)

result = 0

t_cal = 0
t_cost = 0

for j in tcal:
    t_cal = t_cal + j
    t_cost = t_cost + b

    c = (dcal+t_cal) / (a + t_cost)

    if result > c:
        break
    else:
        result = c

print(int(result))
    
