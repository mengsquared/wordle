fiveletterwords=[]
with open('5letterwords') as file:
    for word in file:
        fiveletterwords.append(word.rstrip())
lettercountarray=[dict() for x in range(5)]
for word in fiveletterwords:
    for x in range(5):
        if word[x] in lettercountarray[x]:
            lettercountarray[x][word[x]]=lettercountarray[x][word[x]] +1
        else: 
            lettercountarray[x][word[x]]=1
for dictionary in lettercountarray:
    dictionary={k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    print("START OF DICTIONARY")
    for letter in dictionary:
        print(letter + ',' + str(dictionary[letter]))

letterscorearray=[dict() for x in range(5)]
totallettercount=len(fiveletterwords)
for x in range(5):
    for letter in lettercountarray[x]:
       letterscorearray[x][letter] = lettercountarray[x][letter] /totallettercount

for dictionary in letterscorearray:
    dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    print("START OF DICTIONARY")
    for letter in dictionary:
        print(letter + ',' + str(dictionary[letter]))

wordscore={}
for word in fiveletterwords:
    wordscore[word]=1
    for x in range(5):
        wordscore[word]=letterscorearray[x][word[x]]*wordscore[word]
wordscore={k: v for k, v in sorted(wordscore.items(), key=lambda item: item[1])}
for word in wordscore:
    print(word + ',' + str(wordscore[word]))
    
