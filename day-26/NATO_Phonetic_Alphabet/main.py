import pandas
nato_alphabet_data = pandas.read_csv("NATO_Alphabet_Project\\nato_phonetic_alphabet.csv")
dictionary={row.letter:row.code for (index, row) in nato_alphabet_data.iterrows()}
word= input("Enter a word to make NATO phonetic of ? ")
phonetic_list=[]
for letter in word:
    phonetic_list=[dictionary[letter.upper()] for letter in word]
print(phonetic_list)