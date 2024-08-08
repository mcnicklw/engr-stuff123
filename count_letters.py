dict ={}
count_letters = input(str()).upper()
print(dict)
for letter in count_letters:
    dict[letter] = dict.get(letter, 0) + 1
print(dict)