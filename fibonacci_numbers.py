test = int(input())

n1 = 1
n2 = 1

for i in range(2, test):
    fibbo = n1+n2

    n1 = n2
    n2 = fibbo

print(fibbo)