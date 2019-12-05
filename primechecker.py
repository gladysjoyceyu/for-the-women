num = 6857
x = 2
prime = True
while (x <= int(num/x)):
    if num % x == 0:
        prime = False
        break
    x += 1
if prime:
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))