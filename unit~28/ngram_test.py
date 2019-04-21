text = 'this is python script'
words = text.split()

print(list(zip(words, words[1:])))

text = 'Hello'
two_gram = zip(text, text[1:], text[2:])
for i in two_gram:
    print(i[0], i[1], i[2], sep='')

print(list(zip(*[text[i:] for i in range(3)])))

n = 7 #int(input())
text = 'Python is a programming language that lets you work quickly' #input()
words = text.split()           
 
if (n > len(words)):
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)
