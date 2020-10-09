import sys

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ゃ', 'ゅ', 'ょ', 'っ']
katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ジ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ャ', 'ュ', 'ョ', 'ッ']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０']
punctuation = ['！', '＠', '＃', '＄', '％', '＾', '＆', '＊', '（', '）', 'ー', '＿', '＝', '＋', '「', '」', '￥', '；', '’', '、', '。', '・', '＜', '＞', '？', '｛', '｝', '｜', '｀', '〜', '/', '*', '-', '　', '	']

arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i]

def findSubject(arg):
    possibleSubjects = []
    for i in range(0, len(arg)):
        if arg[i] == 'は':
            possibleSubjects.append(arg[0:i-1])

    for s in possibleSubjects:
        if s[0] in katakana:
            # TODO: search through katakana dictionary
        elif s[0] in hiragana:
            # TODO: search through hiragana dictionary
        else:
            # TODO: search through onKanjiDict.txt
            # TODO: search through kunKanjiDict.txt

    if len(possibleSubjects) >= 1:
        print('Possible subject(s): ' + str(possibleSubjects))
        sub = input('Please enter the number of the correct subject from 0 to ' + str(len(possibleSubjects)) + ': ')
        if sub != '' and sub >= 0 and sub < len(possibleSubjects):
            subject = possibleSubjects[sub]
            return subject
        else:
            return ''

def findObject(arg):
    possibleObjects = []
    for i in range(0, len(arg)):
        if arg[i] == 'が':
            possibleSubjects.append(arg[0:i-1])

    for o in possibleObjects:
        if o[0] in katakana:
            # TODO: search through katakana dictionary
        elif o[0] in hiragana:
            # TODO: search through hiragana dictionary
        else:
        # TODO: search through onKanjiDict.txt
        # TODO: search through kunKanjiDict.txt
    if len(possibleObjects) >= 1:
        print('Possible subject(s): ' + str(possibleObjects))
        ob = input('Please enter the number of the correct subject from 0 to ' + str(len(possibleObjects)) + ': ')
        if ob != '' and ob >= 0 and ob < len(possibleObjects):
            obj = possibleSubjects[ob]
            return obj
        else:
            return ''

subject = findSubject(arg)
obj = findObject(arg)

if subject == '' and obj == '':
    # TODO: continue with implied subject/object case
elif subject != '' and obj == '':
    # TODO: continue with only subject
elif subject == '' and obj != '':
    # TODO: continue with only object
elif subject != '' and obj != '':
    # TODO: continue with subject and object
