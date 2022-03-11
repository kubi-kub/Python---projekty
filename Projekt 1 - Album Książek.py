class Statistics:
    def __init__(self):
        self.LetterCount = 0
        self.LetterDictionary = {}
        for code in range(65, 91):
            self.LetterDictionary[chr(code)] = 0
        self.WordCount = 0
        self.WordDictionary = {}
        self.CurrentWord = ""
        self.CurrentSentence = ""
        self.LongestLetterSentence = ""
        self.ShortestLetterSentence = ""
        self.LongestWordSentence = ""
        self.ShortestWordSentence = ""

    def incrementLetterCount(self):
        self.LetterCount += 1

    def updateLetterDictionary(self, s):
        if s in self.LetterDictionary.keys():
            self.LetterDictionary[s] +=1
        else:
            self.LetterDictionary[s] = 1

    def incrementWordCount(self):
        self.WordCount += 1

    def updateWordDictionary(self, word):
        if word in self.WordDictionary.keys():
            self.WordDictionary[word] += 1
        else:
            self.WordDictionary[word] = 1

def isPolishLetter(s):
    polishCodes = [211, 243, 260, 261, 262, 263, 280, 281, 321, 322, 323, 324, 346, 347, 370, 377, 378, 380]
    polishLetters = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ż", "ź", "Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ż", "Ź"]
    # if ord(s) in polishCodes:
    if s in polishLetters:
        return True
    else:
        return False

def isForeignLetter(s):
    frenchLetters = ["à", "â", "ç", "é", "è", "ê", "ë", "î", "ï", "ô", "û", "ù", "ü", "ÿ", "À", "Â", "Ç", "É", "Ê", "Ë", "Î", "Ï", "Ô", "Û", "Ù", "Ü"]
    germanLetters = []
    czechLetters = []
    danishLetters = []
    spanishLetters = []
    portugueseLetters = []
    if s in frenchLetters or s in germanLetters or s in czechLetters or s in danishLetters or s in spanishLetters or s in portugueseLetters:
        return True
    else:
        return False

def isLetter(s):
    if s != "":
        if 65 <= ord(s) <= 90:
            return True
        elif isPolishLetter(s):
            return True
        elif isForeignLetter(s):
            return True
        else:
            return False
    else:
        return False

def isWordPart(s):
    if isLetter(s) or s in ["-", "'", "`", "’"]:
        return True
    else:
        return False

def isSentenceEnd(s):
    if s in [".", "?", "!", ""]:
        return True
    else:
        return False

def getLetterNumber(sentence):
    count = 0
    for i in range (0, len(sentence)):
        if isLetter(sentence[i]):
            count += 1
    return count

def getWordNumber(sentence):
    count = 0
    sent = ""
    for i in range(0, len(sentence)):
        if isLetter(sentence[i]):
            sent = sent + sentence[i]
        else:
            sent = sent + " "
    return len(sent.split(" "))

def letterAnalysis(s,stat):
    if isLetter(s):
        stat.incrementLetterCount()
        stat.updateLetterDictionary(s)
    return()

def wordAnalysis(s,stat):
    if isWordPart(s):
        stat.CurrentWord = stat.CurrentWord + s
    else:
        if stat.CurrentWord != "":
            stat.incrementWordCount()
            stat.updateWordDictionary(stat.CurrentWord)
            stat.CurrentWord = ""
    return()

def sentenceAnalysis(s, stat):
    if isSentenceEnd(s):
        if stat.CurrentSentence != "":
            if stat.ShortestLetterSentence == "":
                stat.ShortestLetterSentence = stat.CurrentSentence
                stat.LongestLetterSentence = stat.CurrentSentence
                stat.ShortestWordSentence = stat.CurrentSentence
                stat.LongestWordSentence = stat.CurrentSentence
            if getLetterNumber(stat.CurrentSentence) < getLetterNumber(stat.ShortestLetterSentence):
                stat.ShortestLetterSentence = stat.CurrentSentence
            if getLetterNumber(stat.CurrentSentence) > getLetterNumber(stat.LongestLetterSentence):
                stat.LongestLetterSentence = stat.CurrentSentence
            if getWordNumber(stat.CurrentSentence) < getWordNumber(stat.ShortestWordSentence):
                stat.ShortestWordSentence = stat.CurrentSentence
            if getWordNumber(stat.CurrentSentence) > getWordNumber(stat.LongestWordSentence):
                stat.LongestWordSentence = stat.CurrentSentence
            stat.CurrentSentence = ""
    else:
        if stat.CurrentSentence != "" or isLetter(s):
            stat.CurrentSentence = stat.CurrentSentence + s
    return()

def shawnStatistics(stat):
    print("Ilość liter w tekście: " + str(stat.LetterCount))
    maxCount = 0
    letter = ''
    for s in stat.LetterDictionary.keys():
        if stat.LetterDictionary[s] > maxCount:
            letter = s
            maxCount = stat.LetterDictionary[s]
    print("Najczęstsza litera to " + letter + ", która występuje " + str(maxCount) + " razy.")

    print("Ilość słów w tekście: " + str(stat.WordCount))
    maxCount = 0
    word = ''
    for s in stat.WordDictionary.keys():
        if stat.WordDictionary[s] > maxCount:
            word = s
            maxCount = stat.WordDictionary[s]
    print("Najczęstsze słowo to " + word + ", które występuje " + str(maxCount) + " razy.")

    print("Zdanie, które ma najwięcej słów to:", stat.LongestWordSentence)
    print("Zdanie, które ma najmniej słów to:", stat.ShortestWordSentence)

    print("Zdanie, które ma najwięcej liter to:", stat.LongestLetterSentence)
    print("Zdanie, które ma najmniej liter to:", stat.ShortestLetterSentence)


stat = Statistics()

sciezka = 'C:\\Users\\48691\\Desktop\\'
plik = sciezka + 'Janko_Muzykant.txt'
fo = open(plik, 'r', encoding= 'utf8')

while 1:
    s = fo.read(1)
    if s == '':
        wordAnalysis('', stat)
        sentenceAnalysis('', stat)
        break
    else:
        s = s.upper()
        letterAnalysis(s, stat)
        wordAnalysis(s, stat)
        sentenceAnalysis(s, stat)

shawnStatistics(stat)
# print(stat.LetterDictionary)
# print(stat.WordDictionary)


fo.close()