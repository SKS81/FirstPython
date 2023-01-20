print("Hello, world!")
a = 1
print(a)
hello = "Привет, мир!"
print(hello)
b = a + 4
print()  # вывод пустой строки
print(b)
print(a + b)
print()
print("2 в степени 8 =", 2 ** 8)
print(2 ** 8)

# разные способы ввода переменных
s1 = "hello"
s2 = 'hello'
s3 = """hello"""

print(s1)
print(s2)
print(s3)

# объединение переменных
greeting = "Hello " + "world"
print(greeting)

# вычисление длины строки
l = len(greeting)
print(l)
print(len(s1))

# создание списков
strings = ["Hello", "world"]
numbers = [1, 2, 3, 4, 5]
data = ["hello", 1]

print(strings)
print(numbers)
print(data)

# объединение списков
summa = numbers + data
print(summa)

# добавление элементов в список
numbers.append(6)
print(numbers)

# получение доступа к элементу списка по его индексу (с нуля)
first = strings[0]
second = strings[1]
print(first)
print(second)

# получение количества элементов списка
strings_length = len(strings)
print(strings_length)

# суммирование элементов списка
s = sum(numbers)
print(s)
#второй вариант суммирования
summ = 0
for i in numbers:
    summ += i
print(summ)

# создание словарей
dictionary = {
    "cat": "кошка",
    "bat": "летучая мышь"
}
print(dictionary)
cat = dictionary["cat"]
print(cat)

countries = {
    "Африка": ["Египет", "Конго", "ЮАР"],
    "Азия": ["Китай", "Тайланд", "Индонезия"]
}
africa = countries["Африка"]
print(africa)
africa_key = "Африка"
print(countries[africa_key])

# дополнение словарей
countries["Европа"] = ["Австрия", "Испания", "Италия"]
print(countries)
print(countries["Европа"])
# countries[0] = "Hello"
# print(countries)

# добавление элементов
africa.append("Эфиопия")
print(africa)
print(countries)
print(len(countries["Африка"]))

# ввод данных с клавиатуры
name = input("Введите имя: ") #пример ввод текста
print("Здравствуйте,", name, "!")
year = int(input("Укажите год Вашего рождения: ")) #пример ввода целого числа (int)
print("О, Вам уже",2023 - year,")))")

#вывод строки несколько раз (5)
str = "Хай!"
print(str*5)