with open('output.txt') as output:
    lines = output.readlines()
array = lines
array2 = [[]]
for i in array:
    array2.append(i.split(" "))
result = [[]]
for i in array2:
    result.append(list(filter(None,i)))
result = result[2:]
print(result)
for i in result:
    i[1] = i[1].replace("\n" , "")

for i in result:
    print(i[0])

for j in result:
    print(j[1])

