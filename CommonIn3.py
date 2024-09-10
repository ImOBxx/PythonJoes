a = {1, 2, 3, 4, 5}
b = {5, 3, 7, 8, 9}
c = {6, 7, 8, 9 ,10}
t = set()
l = set()

for i in a:
    for j in b:
        if i == j:
            l.add(i)

        for k in c:
            if i == j == k:
                t.add(i)
print("Set 1 & 2 Common: ", l)   
print("Set 1 & 3 Common: ", t)
 

