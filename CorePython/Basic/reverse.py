n=1234
rem=0
rev=0
numbers=n

while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print('reverse number:',rev)
    