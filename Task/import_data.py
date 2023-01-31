all_classes = {}
all_students = {}
id_student = 1

def create_student():
    global id_student
    global all_students
    global all_classes

    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    patronymic  = input("Введите отчество ученика: ")
    birthday = input("Введите дату рождения ученика: ")
    phone = input("Введите номер телефона ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите класс ученика: ")
    if class_name not in all_classes:
        create_class(class_name)
    all_classes[class_name].append(id_student)
    st_data = [surname, name, patronymic, birthday, phone, adress, class_name]
    all_students[id_student] = st_data
    id_student += 1
    return st_data

def create_class(name_class=False):
    if not name_class:
        name_class = input("Введите название класса: ")
    all_classes[name_class] = []

def edit_student():
    student_id = int(input("Введите id студента: "))
    surname = input("Введите исправленную фамилию ученика: ")
    name = input("Введите исправленное имя ученика: ")
    patronymic  = input("Введите исправленное отчество ученика: ")
    birthday = input("Введите исправленную дату рождения ученика: ")
    phone = input("Введите исправленный номер телефона ученика: ")
    adress = input("Введите исправленный адрес ученика: ")
    class_name = all_students[student_id][-1]
    new_st_data = [surname, name, patronymic, birthday, phone, adress, class_name]
    all_students[student_id] = new_st_data
    

def edit_class():
    global all_classes
    global all_students

    student_id = int(input("Введите id студента: "))
    old_class_number = all_students[student_id][-1]
    new_class_number = input("Введите номер нового класса: ")
    
    all_classes[old_class_number].remove(student_id)
    all_classes[new_class_number].append(student_id)

def delete_student():
    student_id = int(input("Введите id студента: "))
    global all_classes
    global all_students
    all_classes[all_students[student_id][-1]].remove(student_id) 
    del all_students[student_id]
    
    