a=int(input())
b=int(input())
try:
    print(a/b)
except ZeroDivisionError:
    print("Ошибка деления на ноль")
except ValueError:
    print("Неверное значение")
except Exception:
    print("Неизвестная ошибка")
else:
    print("Успешное выполнение операции")
print("Программа завершена")