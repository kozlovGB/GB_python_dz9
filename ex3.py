#3. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
some_list=['ключ', 'рыба','лось','мартини']
some_dict={}
print(some_dict.keys())
def transformation_list(some_list=some_list):
    for i in some_list:
        some_dict.setdefault(i,i)
    return some_dict
print(transformation_list())