import string

a = input()
b = a.strip(string.punctuation).replace(',', '').replace('.', '')
#print(b)
c = b.split(' ')

count = c.count('the')
#print(c)
print(count)

