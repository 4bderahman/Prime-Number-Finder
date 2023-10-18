n = int(input("Please enter an integer n: "))

print(f"The prime numbers less than {n} are:")

if n >= 2:
    print(2)

for a in range(3, n, 2):
    for i in range(3, a, 2):
        if a % i == 0:
            break
    else:
        print(a)
