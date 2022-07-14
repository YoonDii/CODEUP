#출석 번호를 n번 무작위로 불렀을 때, 
# 부른 번호를 거꾸로 출력해 보자.

n = int(input())
k = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    print(k[i],end=' ')