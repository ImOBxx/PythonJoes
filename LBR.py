print ()
v = input ("Enter Choice (C / R): ")
if (v == 'R' or v == 'r'):
   l = int (input ("Enter Length: "))
   w = int (input ("Enter Breadth: "))
   print ()
   a = l * w
   p = 2 * (l + w)
   print ("Area Of Rctangle: ", a)
   print ("Perimeter Of Rectangle: ", p)
   print ()

elif (v == 'C' or v == 'c'):
   r = int (input ("Enter Radius: "))
   print ()
   area = 3.14 * r * r
   peri = 2 * 3.14 * r
   print ("Area Of Circle: ", area)
   print ("Circumference Of Circle: ", peri)
   print ()


