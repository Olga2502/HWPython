count = 0
p = 1
for x in range(0, 11):
    x = int(input())
    if x > 0 and abs(x) <= 10 ** 6:
        p = p * x
    count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')