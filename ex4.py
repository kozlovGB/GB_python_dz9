#4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
my_dict={'first_one':'we can do it'}
def biggest_dict(my_dict=my_dict):
    while True:
        some_key=input('Введите ключ')
        if some_key=="":
            break
        some_word=input('Введите слово')
        my_dict.setdefault(some_key,some_word)
    return my_dict


print(biggest_dict())