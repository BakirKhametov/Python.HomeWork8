import new_chek





def user_menu(user_choose):
    print('''Добро пожаловать в справочник школы!
                Выберите действие:
                1. Добавить
                2. Редактировать
                3. Удалить
                4. Вывести в консоль
                5. Экспорт
                6. Выход''')
    user_choose = int(input("Введите номер нужного Вам пункта: "))
    return user_choose
    
    # new_student = '1. Добавить нового студента'
    # change_student = '2. Изменить данные студента'
    # del_student = '3. Удалить студента'
    # view_in_console = '4. Вывести в консоль'
    # export_data = '5. Экспортировать данные в файл'
    # to_exit = '6. Выход'
    # print(f'{new_student}\n\n{change_student}\n{del_student}\n{view_in_console}\n{export_data}\n{to_exit}')
    # return new_chek.digit_check()

    