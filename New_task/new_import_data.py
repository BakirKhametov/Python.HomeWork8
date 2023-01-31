all_classes = {}
all_students = {}
id_student = 0




def create_student():
    global all_students
    global all_classes
    global id_student
   
    
    
    surname = input("Введите фамилию ученика: \n")
    name = input("Введите имя ученика: \n")
    patronymic  = input("Введите отчество ученика: \n")
    birthday = input("Введите дату рождения ученика: \n")
    phone = input("Введите номер телефона ученика: \n")
    adress = input("Введите адрес ученика: \n")
    class_name = input("Введите класс ученика: \n")
    # if class_name not in all_classes:
    #        create_class(class_name)
    # all_classes[class_name].append(id_student)
    id_student += 1
    st_data = [id_student, surname, name, patronymic, birthday, phone, adress, class_name]
    
    return st_data



# def create_class(name_class=False):
#     global all_classes
#     if not name_class in all_classes:
#         name_class = input("Введите название класса: ")
#     all_classes[name_class] = []

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
    

# def edit_class():
#     global all_classes
#     global all_students

#     student_id = int(input("Введите id студента: "))
#     old_class_number = all_students[student_id][-1]
#     new_class_number = input("Введите номер нового класса: ")
    
#     all_classes[old_class_number].remove(student_id)
#     all_classes[new_class_number].append(student_id)

def delete_student():
    global all_students

    student_id = int(input("Введите id студента: "))
    # global all_classes
    
    # all_classes[all_students[student_id][-1]].remove(student_id) 
    del all_students[student_id]
