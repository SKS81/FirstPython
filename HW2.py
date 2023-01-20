HELP = """
help - справка по программе.
add - добавить задачу.
show - вывести все задачи.
exit - выход из программы"""

tasks = []
today = []
tomorrow = []
other = []

run = True
while run:
    command = input("Ведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Мои задачи: ")
        print("Список 'tasks'", tasks)
        print("Список 'today'", today)
        print("Список 'tomorrow'", tomorrow)
        print("Список 'other'", other)
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название новой задачи: ")
        if date == "Сегодня":
            today.append(task)
            print("Задача", task, "добавлена в список 'today'.")
        elif date == "Завтра":
            tomorrow.append(task)
            print("Задача", task, "добавлена в список 'tomorrow'.")
        else:
            other.append(task)
            print("Задача", task, "добавлена в список 'other'.")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неподдерживаемая команда.")
        run = False
print("Завершение приложения.")