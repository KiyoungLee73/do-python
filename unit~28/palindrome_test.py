word = input('단어를 입력하세요: ')
 
print(word == word[::-1])

print(list(word) == list(reversed(word)))