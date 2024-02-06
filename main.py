def local():
   x = 5  # локальная переменная
   print(x)
x = 10 #глобальная переменная
local() #тут результат будет "5" из локальной переменной
print(x) #тут результат "10" из глобальной переменной


def local():
  print(z)
z = 10
local() #Программа не найдет значения Z так как в функции мы её не указали и выдаст значение из глобальной
print(z) #поэтому в ответе получим там 10 и тут 10


q = 3
def func():
   global q # объявляем что теперь значение переменной из функции будет глобальным
   print(q) #тк мы вызываем переменную до объявления её значения то при вызове функции ответ даст из старой то есть 3
   q = 5
   q += 5
   return q

func() #старое значение переменной выдаст как объяснено в 19 строке
print(q) #выдаст новое значние так как поменяли то есть ответ 10


def get_my_func():
   def hello_world():
       print("Hello")
   return hello_world

hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello


def get_mul_func(m):
    nonlocal_m = m
    def local_mul(n): #функция внутри функции
        return n * nonlocal_m

    return local_mul

two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
c = two_mul(5)  # 5 * 2      без переменной не даст результат запомни
print(c)

def func(a, b, c):
   print('a =', a)
   print('b =', b)
   print('c =', c)

func(1, 2, 3)#тут значения аргументов зависят от записанных нами чисел
func(3, 2, 1)
func(a=1, b=2, c=3)#но можно обращаться к ним прямо по имени
func(c=3, b=2, a=1)


v = [1, 2, 3]
g = [v, 4, 5, 6] #тут список войдет в список
print(g)
# [[1, 2, 3], 4, 5, 6]

v = [1, 2, 3]
g = [*v, 4, 5, 6]# а тут благодаря "*" войдет просто значение списка без скобок
print(g)
# [1, 2, 3, 4, 5, 6]

print(v)# [1, 2, 3]
print(*v) # 1 2 3 по тому же принципу


def adder(*nums): #без "*" будет ошибка. Одна "*" для кортежей а две "*" для словарей
    sum_ = 0
    for n in nums:
        sum_ += n #Суммируем аргументы меж собой

    return sum_
print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6

def incorrect_func(name_arg=[]):
   # name_arg является локальной переменной
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
incorrect_func()
print('-----')
incorrect_func() #а тут уже ответы почему-то другие поэтому надо обходить эту тему следующим образом

# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])