def palindrome(num):
    str_num = str(num)
    lstr = len(str_num) - 1 
    x = c = 0
    palindrome = True
    while x + c <= lstr - c:
       
        if(str_num[x+c] != str_num [lstr-c]):
            #print(str_num[x+c] + str_num[lstr-c])
            palindrome = False
        c += 1
    return palindrome

num1 = num2 = largest = 0
for num1 in range(0, 1000):
    for num2 in range(0, 1000):
        mult = num1 * num2
        if (palindrome(mult)):
            if mult > largest:
                largest = mult
        num2 += 1
    num1 += 1
print (largest)