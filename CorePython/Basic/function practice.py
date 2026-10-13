# def _is_armstrong(number):
#     rem = 0
#     sum = 0
#     temp = number
#
#     while temp > 0:
#         rem = temp % 10
#         sum = sum + (rem * rem * rem)
#         temp = temp // 10
#
#     if sum == number:
#         print("armstrong number",number)
#     else:
#         print("not armstrong number",number)
#
# _is_armstrong(157)
#
# def __is__fibonacci(a,b):
#     print(a)
#     print(b)
#
#     for i in range(10):
#         c = a + b
#         print(c)
#         a = b
#         b = c
# __is__fibonacci(0,1)
#

# def add(a,b):
#     print((a+b)*90)
# add(10,20)

# def add(a,b):
#     return a+b
# x=add(10,20)
# print(x*8)
#
# def _is_palindrome(number):
#     rem = 0
#     rev = 0
#     temp = number
#
#     while temp > 0:
#         rem = temp % 10
#         rev = (rev * 10) + rem
#         temp = temp // 10
#
#     if rev == number:
#         print("palindrome number")
#     else:
#         print("not palindrome number")
#
#
# _is_palindrome(121)

# def div(n):
#    for i in range (0,n+1):
#     if i%7==0:
#         print("7 se division:" ,i)
# div(100)


# def remove_number(numbers):
#     numbers.remove(30)
#     print(numbers)
# remove_number([10,20,30,40,50,60,70])
#

# def _reverse_number(n):
#    rem = 0
#    rev = 0
#    temp = n
#
#    while temp > 0:
#       rem = temp% 10
#       rev = (rev * 10) + rem
#       temp = temp // 10
#    print('reverse number:', rev)
# _reverse_number(1234)
#
# def _prime_number(n):
#   count=0
#
#   for i in range (2,n):
#     if n % i == 0:
#         count = count + 1
#   if count==0:
#     print("prime number")
#   else:
#     print("not prime number")
# _prime_number(11)
# #
#
#
# def _maximum_number(a,b):
#    if a<b:
#         print("maximum number:",b)
#    else:
#         print("minimum number:",a)
#
# _maximum_number(10,20)
#
#
# def _odd_number(a):
#
#
#     if a % 2 != 0:
#         print("odd number:", a)
#     else:
#         print("even number:", a)
# _odd_number(20)



