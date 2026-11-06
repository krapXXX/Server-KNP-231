# вступ до Python 
# Install: https://www.python.org/downloads/
print ("hello, world")
# repl read-evaluate-print-loop
# 4gl(слабка типізація, clr у т.ч. контроль ресурсів, GC)
x = 10 # змінні з'являються під час ініціалізації, оголошення не потребують
print(x, type(x)) # 10 <class'int'>
x = 1 + 2j          # мат. орієнтованість - підтримка комплексних чисел
print(x, type(x))   # (1+2j) <class 'complex'>
# Парадигма - множинна, основна - функціональна,
# також ООП - (прототипний варіант),
# також процедурна
x = "hello, world"
print(x, type(x)) # hello, world <class 'str'>
# print(x + 1)     # TypeError: can only concatenate str (not "int") to str
# print(1 + x)     # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Одна з ознак функціональної парадигми - залежність операторів від порядку даних
# Сувора типізація - відсутність неявного перетворення типів, вимога
# передавати той тип даних, що вимагається
print(x+str(1)) # hello, world1 - явне перетворення типів 
x = input ("x = ") # введення з консолі
print(x, type(x)) # 10 <class'str'>
print(int(x) + 1)  # 11 -- явне перетворення типів
x = 1e-2
print(x, type(x))  # 0.01 <class 'float'>
x = 111111111111111111111111111111111111111111111111111111111111111111111111111111
print(x, type(x))  # ... <class 'int'> -- обмежень на розмір чисел немає
x = """The
Multiline
string"""
# розділення команд - з нового рядка - через ";"б але не є поширеним
x = 10; y = 20
print(x,y)
x = (1,2,3)
print(x, type(x))  # (1, 2, 3) <class 'tuple'> -- кортеж - незмінна послідовність
# x[0] = 0         # TypeError: 'tuple' object does not support item assignment
x = [1, 2, 3]
print(x, type(x))  # [1, 2, 3] <class 'list'> -- перелік послідовність з
x[0]=0             # можливістю венсення змін
print(x, type(x))  # [0, 2, 3] <class 'list'>
x = {1, 2, 3}
print(x, type(x))  # [0, 2, 3] <class 'set'> --множина - послідовність унікальних даних
x = {'a': 10, 'b': 20}
print(x, type(x))  # {'a': 10, 'b': 20} <class 'dict'> -- асоціативний масив (ключ:значення)