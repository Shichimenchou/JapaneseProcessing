import os
import sys

wordLength = input('Enter kanji word length: ')
flag = False
kanjiListName = ''
while not flag:
	flag = False
	kanjiListName = input('Enter kanji list: ')
	if os.path.isfile(kanjiListName + '.txt')
		flag = True
	else:
		print('The kanji list given does not exist. Try again.')


f = open(kanjiListName + '.txt', 'r')
kanji = f.readlines()
f.close()

kanjiList = []
for i in kanji:
	kanjiList.append(i.split())

for length in range(1, wordLength):
	# Choose [length] kanji from kanjiList to try combinations of
