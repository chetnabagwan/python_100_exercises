def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a
 
print(acceleration(0,15,0,20))