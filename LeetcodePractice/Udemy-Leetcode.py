num = [0,0,0,1,1,2,3,3,3,3,5,5,5]
i,j = 0, 1
k = 1
while i< j and j < len(num):
    if num[i] == num[j]:
        j += 1
    else:
        i = j
        j += 1
        k += 1
print(k)