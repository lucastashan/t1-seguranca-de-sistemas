# import collections
# import pprint
import os

alph = "abcdefghijklmnopqrstuvwxyz"


def isLetter(char):
    return (char in alph)


def countLetters(text):
    count = 0
    for i in text:
        if(isLetter(i)):
            count += 1
    return count


def getLetterIndex(letter):
    return alph.index(letter)


def getLetter(index):
    return alph[index]


def getIOC(text):
    letterCounts = []

    # Loop through each letter in the alphabet - count number of times it appears
    for i in range(len(alph)):
        count = 0
        for j in text:
            if j == alph[i]:
                count += 1
        letterCounts.append(count)

    # Loop through all letter counts, applying the calculation (the sigma part)
    total = 0
    for i in range(len(letterCounts)):
        ni = letterCounts[i]
        total += ni * (ni - 1)

    N = countLetters(text)
    c = 26.0  # Number of letters in the alphabet
    total = float(total) / ((N * (N - 1)))
    return total


def get_files_in_folder(dir_path):
    res = []
    # Iterate directory
    for file_path in os.listdir(dir_path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(dir_path, file_path)):
            # add filename to list
            res.append(file_path)
    return res


# files = get_files_in_folder('textos/')
# iocs = {}

# for file in files:
# 	file_path = 'textos/' + file
# 	with open(file_path, 'r') as texto:
# 		texto = texto.read()
# 		iocs[file] = round(getIOC(texto), 3)

# print(iocs)
