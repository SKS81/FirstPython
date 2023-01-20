# создание функций
def multiply(a, b):
    return a * b
    #result = a * b
    #return result

c = multiply(4, 5)
print(c)

def print_hello():
    print("Hello")
    print("World")

print_hello()



# наша программа
import random

HELP = """
чаво - справка по программе.
доб - добавить задачу.
все - вывести все задачи.
вых - выход из программы.
randTask - добавить случайную задачу.
randDate - добавить случайную дату.
случайно - добавить случайную задачу на случайную дату.
любая иная команда - завершение приложения."""

RANDOM_TASKS = [
    "Записаться на курс в Нетологию",
    "Написать Гвидо письмо",
    "Покормить кошку",
    "Помыть машину"
]
RANDOM_DATES = [
    "сегодня",
    "завтра",
    "послезавтра"
]

tasks = {}

# создадим функцию "add_todo"
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print("Задача", task, "добавлена на дату", date)

run = True
print()
print("Список команд приложения:")
print(HELP)
while run:
    print()
    command = input("Ведите команду: ")
    if command == "чаво":
        print(HELP)
    elif command == "все":
        print()
        date = input("Укажите дату списка: ")
        if date in tasks:
            print()
            print("Ваши задачи на", date, ":")
            for task in tasks[date]:
                print("-", task)
        else:
            print()
            print("Нет задач на указанную Вами дату.")
    elif command == "доб":
        print()
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название новой задачи: ")
        add_todo(date, task)
    elif command == "вых":
        print()
        print("Спасибо за использование!")
        break
    elif command == "randTask":
        print()
        date = input("Введите дату для добавления задачи: ")
        task = random.choice(RANDOM_TASKS)
        add_todo(date, task)
    elif command == "randDate":
        print()
        date = random.choice(RANDOM_DATES)
        task = input("Введите название новой задачи: ")
        add_todo(date, task)
    elif command == "случайно":
        print()
        date = random.choice(RANDOM_DATES)
        task = random.choice(RANDOM_TASKS)
        add_todo(date, task)
    else:
        print()
        print("Неподдерживаемая команда.")
        run = False
print()
print("Завершение приложения.")