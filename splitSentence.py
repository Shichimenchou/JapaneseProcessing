import sys

hiragana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'ゃ', 'ゅ', 'ょ', 'っ']
katakana = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ジ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ャ', 'ュ', 'ョ', 'ッ']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '１', '２', '３', '４', '５', '６', '７', '８', '９', '０']
punctuation = ['！', '＠', '＃', '＄', '％', '＾', '＆', '＊', '（', '）', 'ー', '＿', '＝', '＋', '「', '」', '￥', '；', '’', '、', '。', '・', '＜', '＞', '？', '｛', '｝', '｜', '｀', '〜', '/', '*', '-', '　', '	']

on = open('Dictionaries/onKanjiDict.txt', 'r')
kun = open('Dictionaries/kunKanjiDict.txt', 'r')
kat = open('Dictionaries/katakanaDict.txt', 'r')
hir = open('Dictionaries/hiraganaDict.txt', 'r')

ON = on.readlines()
on.close()
for i in range(0, len(ON)):
    ON[i] = ON[i].split()

KUN = KUN.readlines()
kun.close()
for i in range(0, len(KUN)):
    KUN[i] = KUN[i].split()

KAT = kat.readlines()
kat.close()
for i in range(0, len(KAT)):
    KAT[i] = KAT[i].split()

HIR = hir.readlines()
hir.close()
for i in range(0, len(HIR)):
    HIR[i] = HIR[i].split()


arg = ''
for i in range(1, len(sys.argv)):
    arg += sys.argv[i]

def findSubject(arg):
    possibleSubjects1 = []
    for i in range(0, len(arg)):
        if arg[i] == 'は':
            possibleSubjects1.append(arg[0:i-1])

    possibleSubjects2 = []
    for s in possibleSubjects1:
        if s[0] in katakana:
            for k in KAT:
                if k[0] == s:
                    possibleSubjects2.append(s)
        elif s[0] in hiragana:
            for h in HIR:
                if h[0] == s:
                    possibleSubjects2.append(s)
        else:
            for O in ON:
                if O[0] == s:
                    possibleSubjects2.append(s)
            for K in KUN:
                if K[0] == s:
                    possibleSubjects2.append(s)

    if len(possibleSubjects2) >= 1:
        print('Possible subject(s): ' + str(possibleSubjects2))
        sub = input('Please enter the number of the correct subject from 0 to ' + str(len(possibleSubjects2)) + ': ')
        if sub != '' and sub >= 0 and sub < len(possibleSubjects2):
            subject = possibleSubjects2[sub]
            return subject
        else:
            return ''

def findObject(arg):
    possibleObjects1 = []
    for i in range(0, len(arg)):
        if arg[i] == 'が':
            possibleObjects1.append(arg[0:i-1])

    possibleObjects2 = []
    for o in possibleObjects1:
        if o[0] in katakana:
            for k in KAT:
                if h[0] == s:
                    possibleObjects2.append(o)
        elif o[0] in hiragana:
            for h in HIR:
                if h[0] == s:
                    possibleObjects2.append(o)
        else:
            for O in ON:
                if O[0] == o:
                    possibleObjects2.append(o)
            for K in KUN:
                if K[0] == o:
                    possibleObjects2.append(o)
    if len(possibleObjects2) >= 1:
        print('Possible objects(s): ' + str(possibleObjects2))
        ob = input('Please enter the number of the correct objects from 0 to ' + str(len(possibleObjects2)) + ': ')
        if ob != '' and ob >= 0 and ob < len(possibleObjects2):
            obj = possibleObjects2[ob]
            return obj
        else:
            return ''

def findVerb(arg):
    # TODO: parse the verb at the end of the sentence
    # TODO: match the parsed verb to plain form and definition
    # TODO: default verb if omitted

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


