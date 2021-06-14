dx=[1,-1,0,0]
dy=[0,0,1,-1]

map=[]
for k in range(7):
    map.append(input().split(' '))

def dfs(x,y,k):
    global cnt
    map[x][y]=-1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<7 and 0<=ny<7:
            if map[nx][ny]==k:
                dfs(nx,ny,k)
                cnt+=1

ans=0
for i in range(7):
    for j in range(7):
        if map[i][j]!=-1:
            cnt=1
            dfs(i,j,map[i][j])
            if cnt>=3:
                ans+=1

print(ans)
