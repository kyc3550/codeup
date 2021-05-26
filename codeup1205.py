# https://codeup.kr/problem.php?id=1205&rid=0

a,b = map(int,input().split(' '))
list = []

list.append(a+b)
list.append(b+a)
list.append(a-b)
list.append(b-a)
list.append(a*b)
list.append(b+a)
list.append(a/b)
list.append(b/a)
list.append(a**b)
list.append(b**a)

print('{:.6f}'.format(max(list)))
