import sys
import re

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ゃ', 'ゅ', 'ょ', 'っ']
katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ジ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ャ', 'ュ', 'ョ', 'ッ']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０']
punctuation = ['！', '＠', '＃', '＄', '％', '＾', '＆', '＊', '（', '）', 'ー', '＿', '＝', '＋', '「', '」', '￥', '；', '’', '、', '。', '・', '＜', '＞', '？', '｛', '｝', '｜', '｀', '〜', '/', '*', '-', '　', '	']

arg = ''
for i in range(1, len(sys.argv)):
	arg += sys.argv[i]

dct = open('kanjiDict.txt', 'r')
dictionary = dct.readlines()
dct.close()

rdngs = open('kanjiReadings.txt', 'r')
readings = rdngs.readlines()
rdngs.close()

kanji = ''
for i in arg:
	if i not in hiragana and i not in katakana and i not in numbers and i not in punctuation:
		kanji += i
	else:
		processKanji(kanji)
		kanji = ''


def generateCombinations(array, row):
	combinations = []
	if row == len(array) - 1:
		for i in array[row]:
			combinations.append(i)
	else:
		lowerCombs = generateCombinations(array, row + 1)
		for i in array[row]:
			for j in lowerCombs:
				combinations.append(i + j)
	return combinations
	
	
def processKanji(inp):
	found = ''
	for d in dictionary:
		if inp in d:
			found = d
	if found != '':
		definition = re.split(r'\t+', d)
		toPrint = definition[0] + ' can be read as: '
		possibilities = []
		for i in range(1, len(definition)):
			if definition[i][0] in hiragana:
				possibilities.append(definition[i])
			else:
				toPrint += str(possibilities)
				toPrint += ' and can mean: '
				defs = []
				for j in range(i, len(definition)):
					defs.append(definition[j].strip())
				toPrint += str(defs)
		print(toPrint)
	else:
		toCombine = []
		for c in inp:
			for i in readings:
				if c in i:
					temp = re.split(r'\t+', i)
					kanjiReadings = temp[1:]
					for j in range(0, len(kanjiReadings)):
						kanjiReadings[j] = kanjiReadings[j].strip()
					toCombine.append(kanjiReadings)
					break
		print(toCombine)
		combinations = generateCombinations(toCombine, 0)
		print('Here are all the possible readings of this word:\n')
		print(combinations)
		read = input('Enter the proper reading: ')
		definition = input('Enter the definition: ')
		dictionary.append(inp.ljust(20 - len(inp)) + read.ljust(35 - len(read)) + definition + '\n')
		dd = open('kanjiDict.txt', 'w')
		for ddd in dictionary:
			dd.write(ddd)
		dd.close()
		print(inp + ' has been added to the kanji dictionary.')


processKanji(kanji)
