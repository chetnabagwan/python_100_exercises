d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

#1st way:
for item in d:
    print(item,"has value ",d[item])

#2nd way:
print("  ")
for key,value in d.items():
    print(key, "has value ",value)