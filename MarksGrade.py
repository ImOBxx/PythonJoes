n1 = int (input ("Enter 1st Subject Marks: "))
n2 = int (input ("Enter 2nd Subject Marks: "))
n3 = int (input ("Enter 3rd Subject Marks: "))
n4 = int (input ("Enter 4th Subject Marks: "))
n5 = int (input ("Enter 5th Subject Marks: "))

am = n1 + n2 + n3 + n4 + n5

per = (am / 500) * 100.0

print ("Aggregate Marks: ", am)
print ("Your Percentage: ", round(per))