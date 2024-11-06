calls = 0 #Создаем переменную для подсчета вызовов
def count_calls():
    global calls # Используем глобальную переменную
    calls += 1 # Увеличиваем счетчик вызовов на 1


def string_info(string):
    count_calls() # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())
    # Возвращаем кортеж из длины строки, из строки в
    # верхнем регисре и в нижнем

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    for item in list_to_search:
        if item in string:
            return True
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)