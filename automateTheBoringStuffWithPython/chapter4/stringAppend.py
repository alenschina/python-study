spam = ['apples', 'bananas', 'tofu', 'cats']

string = ''
spamLentgh = len(spam)
lastIndex = spamLentgh - 2
for i in range(0, spamLentgh):
    if(i < lastIndex):
        string += spam[i] + ', '
    elif(i == lastIndex):
        string += spam[i] + ' and '
    else:
        string += spam[i]

print(string)