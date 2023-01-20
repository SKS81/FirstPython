#Алгоритмы и условия
name = input("Введите имя: ")
login = "Саша"
if name == login: # двойное равно - значит "сравнить", выводит True, т.е. равно или False не равно
    print("Привет,", name)
# elif и else взаимоисключаемы, выполняется только первое подходящее условие
elif len(name) < 2:
    print("Слишком короткое имя.")
elif name == "Y":
    print("И тебе Йоу, бро!")
else:
    print("Привет, пользователь")
print("Пока!")

# циклы
i = 0
while i <= 10:
    print(i)
    #i = i + 1
    i += 1

# первая программа
HELP = """
help - справка по программе.
add - добавить задачу.
show - вывести все задачи."""

tasks = []

run = True
while run:
    command = input("Ведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название новой задачи: ")
        tasks.append(task)
        print("Задача успешно добавлена.")
    else:
        print("Неподдерживаемая команда.")
        #run = False
        break
print("Завершение приложения.")