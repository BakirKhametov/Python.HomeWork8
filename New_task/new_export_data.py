import new_import_data as impd
import new_logger as log

def create_data():
    data = impd.create_student()
    log.write_file(data)
    return data

def delete_data():
    data = impd.delete_student()
    log.write_file(data)
    return data

def change_data():
    data = impd.edit_student()
    log.write_file(data)
    return data