data = [4,5,104,105,x110,120,130,130,150,160,
        170,178,183,185,188,191,350,360]

minimum = 100
maximum = 200

stop = 0
begin = 0

for index , value in enumerate(data):
    if value >= minimum:
        stop = index
        break 

del data[:stop]

#data.sort(reverse=True)
print(data)
for index in range(len(data)-1,-1,-1):
    if data[index] <= maximum:
        begin = index + 1
        break
del data[begin:]

#data.sort(reverse = False)
print(data)