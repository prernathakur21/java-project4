n=12
count=0

for i in range (2,11):
    if n % i == 0:
        count = count + 1
if count==0:
    print("prime number")
else:
    print("not prime number")




