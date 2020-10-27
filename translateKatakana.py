import sys
import re

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'ま', 'み', 'む', 'め', 'も', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ゃ', 'ゅ', 'ょ', 'っ']

katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',  'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ジ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ャ', 'ュ', 'ョ', 'ッ']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０']

punctuation = ['！', '＠', '＃', '＄', '％', '＾', '＆', '＊', '（', '）', 'ー', '＿', '＝', '＋', '「', '」', '￥', '；', '’', '、', '。', '・', '＜', '＞', '？', '｛', '｝', '｜', '｀', '〜', '/', '*', '-', '　', '	']

arg = ''
for i in range(1, len(sys.argv)):
	arg += sys.argv[i]

dct = open('Dictionaries/katakanaDict.txt', 'r')
dictionary = dct.readlines()
dct.close()

kat = ''
for i in arg:
    if i in katakana:
        kat += i
    else:
        break

def processKatakana(inp):
    found = ''
    for d in dictionary:
        if inp in d:
            found = d
    if found != '':
        definition = found.split()
        toPrint = definition[0] + ' can be read as: '
        possibilities = []
        for i in range(1, len(definition)):
            if definition[i][0] in katakana:
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
        definition = input('Enter the definition: ')
        dictionary.append(inp.ljust(40 - len(inp)) + definition + '\n')
        dd = open('Dictionaries/katakanaDict.txt', 'w')
        for ddd in dictionary:
            dd.write(ddd)
        dd.close()
        print(inp + ' has been added to the katakana dictionary.')

processKatakana(kat)
