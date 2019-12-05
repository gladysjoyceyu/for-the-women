num = 600851475143
x = 2
while (x <= int(num/x)):
    if num % x == 0:
        y = 2
        prime = True
        while (y <= int(x/y)):
            if x % y == 0:
                prime = False
                break
            y += 1
        if prime:
            largest = x
    x += 1
print (largest)