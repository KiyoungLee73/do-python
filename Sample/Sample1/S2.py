# Calc

input_data = 'L80, M20, H60, M100, L100'
# per hour L : 150, M : 80, H : 50
# Time : 360 min


# Answer
data = map(str, input_data.split(', '))
dic_data = {}
total = 0

for a in data:
    #print(a[0])
    #print(a[1:len(a)])
    if a[0] in dic_data:
        dic_data[a[0]] = dic_data[a[0]] + int(a[1:len(a)])
    else:
        dic_data[a[0]] = int(a[1:len(a)])
#print(dic_data)

for key in dic_data.keys():
    #print(key)
    #print(dic_data[key])
    if key == 'L':
        total = total + dic_data[key] / 60 * 150
    elif key == 'H':
        total = total + dic_data[key] / 60 * 50
    elif key == 'M':
        total = total + dic_data[key] / 60 * 80
    
print(int(total))