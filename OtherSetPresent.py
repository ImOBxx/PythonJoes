x = {50, 20, 70, 40, 10 ,60, 30}
y = {80, 50, 100, 70, 90, 60}
l = []
dup = set()
dup1 = set()
dup2 = set()
for i in x:
    for j in y: 
        if i == j:
            dup.add(i)
print(x - dup)
print(y - dup)


