
num_cases = int(input())

cases = []
for i in range(0,num_cases):
    cases.append(list(input()))


for i, case in enumerate(cases):

    a = case
    b = 0

    for j, digit in enumerate(a):
        if int(a[j]) == 4:
            a[j] = "2"
            b = b + pow(10, len(a)-1 - j) * 2

    print("Case #{}: {} {}".format(1+i, "".join(a), b))

