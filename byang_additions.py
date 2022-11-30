# a = int(input())
# b = int(input())
#
# a_1st_remaining = a % 10
# b_1st_remaining = b % 10
#
# while True:
#
#     if a_1st_remaining + b_1st_remaining > 9:
#         print("yes")
#         break
#     else:
#         a_2nd = int(a / 10)
#         b_2nd = int(b / 10)
#         a_2nd_remaining = a_2nd % 10
#         b_2nd_remaining = b_2nd % 10
#         if a_2nd_remaining + b_2nd_remaining > 9:
#             print("yes")
#             break
#         else:
#             a_3rd = int(a_2nd / 10)
#             b_3rd = int(b_2nd / 10)
#             a_3rd_remaining = a_3rd % 10
#             b_3rd_remaining = b_3rd % 10
#             if a_3rd_remaining + b_3rd_remaining > 9:
#                 print("yes")
#                 break
#             else:
#                 print("No")
#                 break


x = input()

m, n = x.split()

a = list(m)
b = list(n)

a = a[::-1]
b = b[::-1]

count = 0

if len(a) >= len(b):
    n = len(b)
else:
    n = len(a)

for i in range(0, n):
    sum = int(a[i]) + int(b[i])
    if sum > 9:
        count = count + 1
        sum = 0

if count != 0:
    print("Yes")
else:
    print("No")