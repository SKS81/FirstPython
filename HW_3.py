list = [
    "python",
    "c++",
    "c",
    "scala",
    "java"
]

letter = "c"
words_list = []

def count_letter(list):
    count = 0
    for word in list:
        if letter in word:
            count += 1
    return count

def count_words(list):
    for word in list:
        if letter in word:
            words_list.append(word)
    return words_list

summ_words = count_letter(list)
list_words = count_words(list)

print("Количество слов, содержащих букву", letter, ":", summ_words)
print("Список слов, содержащих букву", letter, ":", list_words)



def count_lettersss(listsss, lettersss):
    result = 0
    for word in listsss:
        if lettersss in word:
            result += 1
    return result

print(count_lettersss(['python', 'c++', 'c', 'scala', 'java'], 'c'))