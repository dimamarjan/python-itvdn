# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает произвольное количество именованных параметров.
# Вызовите её с созданным словарём и явно указывая параметры.
def foo(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

my_dict = {
    'key 1':100,
    'key 2':102,
    'key 3': 333
}

foo(key3=100, key2=102, key= 333)

