# print
# СОЗДАНИЕ СОБСТВЕННОЙ ФУНКЦИИ
# def a_ful():
#     '''я простая функция'''
#     print('Привет я функция!')
#
#
# a_ful()


# a = 'hi' # переменную лучше вводить до написания функции, если мы хотим её использовать в нутри функции
# def empty_fun():
#     '''пустая функция'''
#     pass # может понадобится в коде, в дальнейшем можно дописать
#     print(a)
#
# empty_fun()
# a = [1, 5, 6, 10, 3]
#
# def summa_a(a):
#     s = 0
#     for i in a:
#         if type(i) == int:
#             s += i
#     print(s)
#
#
# summa_a()

# a = [1, 1, 2, 4]
# def s_fun():
#     count = 0
#     for i in a:
#         count += i
#     print('сумма в списке: ', count)
#
# s_fun()



# # Усовершенственная функция sum()
# # Сначала пишется функция, а затем можно применять неоднократно к разным спискам
# def s_fun(x):
#     print(x)
#     count = 0
#     for i in x:
#         count += i
#     print('сумма в списке: ', count)
#
# a = [1, 1, 2, 4]
# s_fun(a)
# b = [3, 25, 10, 4]
# s_fun(b)


# def add(a, b):
#     print(a + b)
#     return a + b # чтобы писался результат в print при вызове новой функции вместо None
#
#
# print(add(1, 2))
# x = add(2, 3) # можно создать переменную со значением функции и использовать в дальнейшем как простое число
# print(x)

# def add(a, b):
#     print('a=', a, 'b=',  b) # нужно для удобства записать название('a=' 'b=')
#     return a + b # чтобы писался результат в print при вызове новой функции вместо None
#
#
# print(add(1, 2))
# print(add(1, 3))
# print(add(b=4,a=6)) # числа можно записывать в разном порядке
# x = add(b=7, a=3)
# print(x)

# def add(a, b):
#     print('a=', a, 'b=',  b) # нужно для удобства записать название('a=' 'b=')
#     return a + b
#
# # универсальная функция числа складывает, строки объединяет,
# # а списки объединяет в один(конкотенация)
# print(add(1, 2)) # 3
# print(add('hi', 'world')) # hiworld
# print(add([1, 2, 3], [5, 6, 7])) # [1, 2, 3, 5, 6, 7]



# # МОЖНО СТАВИТЬ ЧИСЛА ПО УМОЛЧАНИЮ add(a=1, b=1)
# def add(a=1, b=1):
#     print('a=', a, 'b=',  b)
#     return a + b
#
# print(add()) # a= 1 b= 1 (2)
# print(add(5)) # a= 5 b= 1 (6) если записать одно число, оно примет значение а, b=1 по умолчанию
# print(add(5, 5))# a= 5 b= 5 (10) можно записать оба числа
# print(add(b=10)) # a= 1 b= 10 (11) можно указать значение второго числа, а=1 по умолчанию
#
# # МОЖНО ОДНО ЧИСЛО СДЕЛАТЬ ИЗМЕНЯЕМЫМ, А ДРУГИЕ ПО УМОЛЧАНИЮ
# def add(e, a=1, b=1):
#     print('e=', e, 'a=', a, 'b=',  b)
#     return a + b + e
#
#
# print(add(10)) # e= 10 a= 1 b= 1 (12)
# print(add(1, 2, 2)) # e= 1 a= 2 b= 2 (5)
# print(add(a=1, b=2, e=2)) # e= 2 a= 1 b= 2 (5)


# def many(*args, **kwargs):  # для использования неограниченного количества функций
#     # args и  kwargs нельзя менять местами, можно использовать по отдельности
#     print(args) # (1, 2, 3, 'ddad', 4) кортеж
#     print(kwargs) # {'a': 12, 'b': 34, 'c': 44} обычный словарь
#
# many(1, 2, 3, 'ddad', 4, a=12, b=34, c=44)

# def many(*args, **kwargs):  # для использования неограниченного количества функций
#     # args и  kwargs нельзя менять местами, можно использовать по отдельности
#     print(args) # (1, 2, 3, 'ddad', 4)
#     for i in args:
#         print(i) # 4
#     print(kwargs) # {'a': 12, 'b': 34, 'c': 44}
#     print(kwargs.values()) # dict_values([12, 34, 44])
#
# many(1, 2, 3, 'ddad', 4, a=12, b=34, c=44)


# # ОБЛАСТЬ ВИДИМОСТИ И ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
# def function_a():
#     global a # переменную можно сделать видимую во всех функциях,
#     # если не сделать видимое и воспользоваться в другой функции, то возникнет ошибка
#     a = 1
#     b = 2
#     return a + b
#
# def function_b():
#     c = 3
#     return a + c
#
# print(function_a())
# print(function_b())


# # ВЛОЖЕННЫЕ ФУНКЦИИ
# def func1(a, b):
#     def inner_func(x):
#         return x * x * x
#
#     return inner_func(a) + inner_func(b)
#
# print(func1(4, 5)) # 4*3 + 5*3 = 189


# # ФУНКЦИЮ М. ЗАПИСАТЬ В ОДНУ СТРОКУ, ЕСЛИ ЮЛОК ИНСТРУКЦИЙ ЭТО ПРОСТОЕ ВЫРАЖЕНИЕ
# def sum(a, b): return a + b
#
#
# print(sum(1, 5)) # 6


# a = int(input('введите номер мясяца: '))
# def season(a):
#
#     if a == 1 or a == 2 or a == 12:
#         print('зима')
#     elif a == 3 or a == 4 or a == 5:
#         print('весна')
#     elif a == 6 or a == 7 or a == 8:
#         print('лето')
#     elif a == 9 or a == 10 or a == 11:
#         print('осень')
#     else:
#         print('в году 12 месяцев')
#     return a


# print(season(a))

#
# def season(a):
#     if 5 < a < 9:
#         print("Это лето")
#     elif 8 < a < 12:
#         print("Это осень")
#     elif a == 12 or a == 1 or a == 2:
#         print("Это зима")
#     elif 2 < a < 6:
#         print("Это весна")
#     else:
#         print("такого месяца не существует)")
#
# a = int(input("Введите номер месяца: "))
#
# season(a)
#
#
#
#
# m = input('введите месяц ')
# def season(m):
#     if int(m) in range(1, 3):
#         print('winter')
#     if int(m) == 12:
#         print('winter')
#     if int(m) in range(3, 6):
#         print('spring')
#     if int(m) in range(6, 9):
#         print('summer')
#     if int(m) in range(9, 12):
#         print('autmn')
#     if int(m)>12:
#         print('нет такого месяца')
#
#
# season(m)




def summa(a, b):
    return  a + b
def raz(a, b):
    return  a - b
def divide(a, b):
    return  a / b
def multyply(a, b):
    return  a * b



while True:
    n = '''
    Выберите операцию:
    + : Сложение
    - : Вычитание
    / : Деление
    * : Умножение
    n : Завершение вычислений

    Ваш выбор: 
    '''
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    oper = input(n)
    if oper == '+':
        print(summa(a, b))
    elif oper == '-':
        print(raz(a, b))
    elif oper == '/':
        if b != 0:
            print(divide(a, b))
        else:
            try:
                b == 0
            except ZeroDivisionError:
                print('Деление на ноль')

    elif oper == '*':
        print(multyply(a, b))
    elif oper == 'n':
        break
        print('Завершение операции')
