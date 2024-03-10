word = input('enter a word: ')
list = list(word)

for i in range(0,len(word)):
    if word[i] in ['s','S']:
        list[i] = ''
        new_word = ''.join(list)
        
print(new_word)
