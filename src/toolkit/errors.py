a=input()
b=input()

#initializing errors
try:
    print(a/b)
except ZeroDivisionError:
    print("Ошибка деления на ноль")
except ValueError:
    print("Неверное значение")
except Exception as e:
    print(e.__class__, e)
else:
    print("Успешное выполнение операции")
print("Программа завершена")