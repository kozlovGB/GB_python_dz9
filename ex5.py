#5. Дана строка в виде случайной последовательности чисел от 0 до 9.
#Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
from collections import Counter
from random import randint
N=int(input('Введите колличество эллементов строки: '))

A = [randint(1,9) for _ in range (N) ]
counter = Counter(A)
some_dict=dict(counter)
print(f"Исходный список: {A}")
print(f"Исходный словарь: {counter}")
def count_it(sequence=some_dict):
    new_sequence={}
    max=-10
    if len(sequence)>3:
        for _ in range(3):
            for f,m in sequence.items():
                if m>max:
                    max=m
                    del_point=f
            new_sequence.setdefault(del_point,max)
            del sequence[del_point]
            max=-9
            del_point=-10
        return new_sequence
    elif len(sequence)==3:
        return sequence
    else:
        print("Функция не может возвратить словарь из 3-х самых часто встречаемых чисел, так как чисел меньше трех")


print((count_it()))