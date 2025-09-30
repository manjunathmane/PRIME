num=int(input("Enter the number:"))
if num % 2 == 0:
    print({num}," is even")
else:
    print({num}," is odd")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)