import export_data as ed
import import_data as impd

def user_choose():
    print('''Добро пожаловать в справочник школы!
                Выберите действие:
                1. Добавить
                2. Редактировать
                3. Удалить
                4. Вывести в консоль
                5. Экспорт
                6. Выход''')
    choose = int(input("Введите цифру выбора: "))
    if choose == 1:
        print('''Выберите действие:
                1. Добавить ученика
                2. Добавить класс''')
        add_choose = int(input("Введите цифру выбора: "))
        if add_choose == 1:
            impd.create_student()
        elif add_choose == 2:
            impd.create_class()
    elif choose == 2:
        print('''Выберите действие:
                1. Редактировать ученика
                2. Перевести в другой класс''')
        edit_choose = int(input("Введите цифру выбора: "))
        if edit_choose == 1:
            impd.edit_student()
        elif edit_choose == 2:
            impd.edit_class()
    elif choose == 3:
        impd.delete_student()
    elif choose == 4:
        ed.to_consoleto_console()
    elif choose == 5:
        ed.to_csv()
    elif choose == 6:
        return
        # print('exit')
    else:
        print("Вы ввели некорректное значение!")
    user_choose()

