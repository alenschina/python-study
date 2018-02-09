import os

madLibsFile = open('libs.txt')
template = madLibsFile.read()
madLibsFile.close()

print('Enter an adjective')
adjective = str(input())

print('Enter a noun')
noun1 = str(input())

print('Enter a verb')
verb = str(input())

print('Enter a noun')
noun2 = str(input())

template = template.replace('ADJECTIVE', adjective)
template = template.replace('NOUN1', noun1)
template = template.replace('VERB', verb)
template = template.replace('NOUN2', noun2)

print(template)

fileName = 'libs_'+adjective+'.txt'
madLibsFile = open(fileName, 'a')
madLibsFile.write(template)
madLibsFile.close()

print('new file created at' + os.path.abspath(os.path.curdir)+fileName)

