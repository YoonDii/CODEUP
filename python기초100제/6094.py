
#출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.


n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)
