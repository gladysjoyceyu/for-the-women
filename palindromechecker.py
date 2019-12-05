num = 90909
str_num = str(num)
lstr = len(str_num) - 1 
x = c = 0
palindrome = True
while x + c <= lstr - c: 
    if(str_num[x+c] != str_num [lstr-c]):
        #print(str_num[x+c] + str_num[lstr-c])
        palindrome = False
    c += 1
if palindrome:
    print("{} is a palindrome".format(num))
else:
    print("{} is not a palindrome".format(num))