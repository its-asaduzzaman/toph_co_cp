a = input()
a_rev = reversed(a)

if list(a_rev) == list(a):
    print("yes")
else:
    print("no")