count  = 0
t_count = 0
print()
print ("Even Numbers: ")
print()
for i in range (1, 101):
    if (i % 2 == 0):
        print (i)
        count = count + 1
print ()
print ("Odd Numbers: ")
print ()
for i in range (1, 101):
    if (i % 2 != 0):
        print (i)
        t_count = t_count + 1

print ("Total Count Of Even Numbers: ", count)
print ("Total Count Of Odd Numbers: ", t_count)
print ()