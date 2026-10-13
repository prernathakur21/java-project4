n = 121
rem = 0
rev = 0
temp = n

while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

if rev == n:
    print("palindrome number")
else:
    print("not palindrome number")


