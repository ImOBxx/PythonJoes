print ()
n = int (input ("Enter Number: "))
sum = 0
while (n > 0):
    r = n % 10
    sum = sum + r
    n = n // 10
print ()
print ("Sum Of Digits: ", sum)
print ()