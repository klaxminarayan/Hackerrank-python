a=int(input())
b=int(input())
c=int(input())
n=int(input())
ans=[[i,j,k] for i in range(0,a+1) for j in range(0,b+1) for k in range(0,c+1) if i+j+k!=n]
print(ans)