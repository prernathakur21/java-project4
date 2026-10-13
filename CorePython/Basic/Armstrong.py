n=157
rem=0
sum=0
temp=n

while temp>0:
    rem=temp%10
    sum=sum+(rem*rem*rem)
    temp=temp//10

if sum==n:
    print("armstrong number")
else:
    print("not armstrong number")