import string


class Word(object):
    def __init__(self, w: str):  ### Конструктор
        self.word = w
        self.amount = 1


def sort_dictionary(w: Word):
    return w.amount


dictionary = []
for line in open('text.txt', 'r', encoding='utf-8'):
    fields = line.split(' ')
    for word in fields:
        if word:
            curr_word = word.rstrip().rstrip(string.punctuation).lower()
            curr_word.rstrip()
            if len(curr_word) >= 4:
                flag = True
                for x in dictionary:
                    if x.word == curr_word:
                        x.amount += 1
                        flag = False
                        break
                if flag:
                    dictionary.append(Word(curr_word))


dictionary.sort(key=sort_dictionary)

print('Частотная характеристика слов:')
for x in dictionary:
    print(x.word, ' ', x.amount)

print('\nНаиболее часто встречаемое слово: ', dictionary[len(dictionary)-1].word)
print('Наименее часто встречающиеся слова:')
minAmount = dictionary[0].amount
for x in dictionary:
    if x.amount == minAmount:
        print(x.word)
    else:
        break