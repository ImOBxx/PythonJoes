print ()
n = int (input ("Enter Number: "))
print ()
sum = 0
r = n % 10

n = n / 1000
r1 = n % 10
print ("First Digit: ", round(r1))
print ("Last Digit: ", r)
add = r + r1
print()

print ("Sum Of First And Last Digit: ", round(add))
print ()