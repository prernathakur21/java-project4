notes = [100, 10, 500, 2, 1, 5, 50, 200]

for i in range(0, len(notes)):
    for j in range(i + 1, len(notes)):
        if notes[i] < notes[j]:
            temp = notes[i]
            notes[i] = notes[j]
            notes[j] = temp

print(notes)
amount = 25266

count = 0

for i in notes:
    count = amount // i
    if count > 0:
        print(i, " = ", count)
    amount = amount % i

# str="prerna is a good girl"
# count=0
# for i in str:
#     if i=="o" and i=="O":
#         count=count+1
# print("count=",count)
#
# #
# a=10
# b=20
# print("before swapping a=",a)
# print("before swapping b=",b)
#
# c=0
# c=a
# a=b
# b=c
# print("after swapping")