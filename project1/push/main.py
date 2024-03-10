word = input('enter a word: ')

for i in range(0,len(word)):
    if word[i] in ['s','S']:
        new_word = word[:i] + '' + word[i+1:]
        print(new_word)
            