
import new_import_data as impd
import new_interface as ui
import new_logger as log
import new_export_data as exd



def user_choose():
    choose = ui.user_menu(user_choose)
    # if choose > 7:
    #     print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
    #     user_choose()
    
    if choose == 1:
        exd.create_data()
    elif choose == 2:
        exd.change_data()
    elif choose == 3:
        exd.delete_data()
    elif choose == 4:
        log.read_file()
    elif choose == 5:
        exd.export_data()
    elif choose == 6:
        exit()
    
