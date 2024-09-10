d = {'Name' : 'Pooja', 'Age' : 23, 'Gender' : None, 'Mark' : 488, 'City' : None}
i = d.keys()
k = d.values()
d = {key: value for (key, value) in d.items() if value is not None}
print(d)