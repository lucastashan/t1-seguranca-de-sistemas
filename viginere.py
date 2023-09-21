import argparse
import indice_de_coincidencia as ic
import math

def get_subtexts(ciphertext, key_length):
    substrings = []
    for i in range(key_length):
        substrings.append(ciphertext[i::key_length])
    return substrings

def decrypt_viginere(ciphertext, key):
    plaintext = ""
    key_index = 0
    for i in ciphertext:
        letter_index = ic.getLetterIndex(i)
        letter_index -= key[key_index]
        letter_index %= 26
        plaintext += ic.getLetter(letter_index)
        key_index += 1
        key_index %= len(key)
    return plaintext

def get_most_frequent_character(text):
    letterCounts = []

    # Loop through each letter in the alphabet - count number of times it appears
    for i in range(len(ic.alph)):
        count = 0
        for j in text:
            if j == ic.alph[i]:
                count += 1
        letterCounts.append(count)

    max_count = max(letterCounts)
    max_index = letterCounts.index(max_count)
    return ic.alph[max_index]

def main():

    """! ArgumentParser routine"""
    parser = argparse.ArgumentParser(usage='python3 viginere.py -f cipher_eng.txt',
                                     description='Viginere decoder.')
    parser.add_argument('-f', '--file_path', required=True,
                        help='Path to the file containing the ciphertext.')

    args = parser.parse_args()


    with open(args.file_path, 'r') as f:
        ciphertext = f.read()

    print(ciphertext[:100])

    # start with key length = 1
    key_length = 1
    subtexts = []

    while key_length < len(ciphertext):
        print('- key length: {}'.format(key_length))
        subtexts = get_subtexts(ciphertext, key_length)
        # for i in range(key_length):
        #     print('IOC of text {}: {}'.format(i, ic.getIOC(subtexts[i])))
        subtexts_ioc = []
        for i in range(len(subtexts)):
            subtexts_ioc.append(ic.getIOC(subtexts[i]))
        average_ioc = sum(subtexts_ioc) / len(subtexts_ioc)
        average = math.floor(average_ioc * 100)/100.0

        print('Average IOC: {}'.format(average))

        if average >= 0.06 and average <= 0.08:
            break

        print('*'*50)
        key_length += 1

    while True:
        key = []
        for i in range(len(subtexts)):
            language_letter = input('Type one letter to the lenguage(most frequent): ')

            most_frequent = get_most_frequent_character(subtexts[i])
            print('Most frequent character in cipher text {}: {}'.format(i, most_frequent))

            language_letter_number = ic.alph.index(language_letter)
            most_frequent_number = ic.alph.index(most_frequent)
            if language_letter_number <= most_frequent_number:
                difference = most_frequent_number - language_letter_number
            else:
                difference = len(ic.alph) - language_letter_number + most_frequent_number

            key.append(difference)

        dec = decrypt_viginere(ciphertext[:100], key)
        for i in range(0, len(dec), len(key)):
            print(dec[i:i+len(key)])

        if input('Press y if the text is readable:') == 'y':
            break

    print(dec)

    with open('text.txt', 'w') as f:
        print('Writing decoded text in text.txt...')
        f.write(decrypt_viginere(ciphertext, key))


if __name__ == '__main__':
    main()
