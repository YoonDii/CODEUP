#정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))

#실수는 두번째자리까지 나오게끔 한다.
