def make_product_name(*args, sep=' ', **kwargs):
    # Создаём список для хранения строковых значений
    result = []

    # Обрабатываем позиционные аргументы
    for arg in args:
        if type(arg) is str:
            result.append(arg)

    # Обрабатываем именованные аргументы
    for key, value in kwargs.items():
        if type(value) is str:
            result.append(value)

    # Соединяем строки с указанным разделителем
    return sep.join(result)

# Пример использования
result = make_product_name('Мужская','Рубашка', 123,
                           color='Синий', size=42, sep='_')
print(result)  # Ожидаемый вывод: 'Мужская_Рубашка_Синий'