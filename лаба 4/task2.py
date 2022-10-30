def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    ansver = {}
    biblioteka = []
    for symbol in str_:
        if (symbol not in biblioteka) and (symbol.isalpha() == True):
            biblioteka += symbol
    for element in biblioteka:
        counter = str_.count(element)
        ansver[element] = ansver.get(element, counter)
    return ansver


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))