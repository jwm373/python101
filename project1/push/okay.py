word = input('enter a word: ')
new_word = ''

for i in range(0,len(word)):
    if word[i] not in ['s','S']:
        new_word += word[i] 

print(new_word)