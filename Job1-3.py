a = {2023, 15000, "Tananchai"} #Set
b = [2023, 15000, "Tananchai"] #List
c = (2023, 15000, "Tananchai") #Tuple
d = {1: 2023, 'Salary':15000, "name": "Tananchai"} #Dictionary

b[1] = 25000
d["salary"] = 35000
print(a)
print(b)
print(c)
print(d)
print(d[1])
print(d["name"])
print(type(d)) #Show Data Type