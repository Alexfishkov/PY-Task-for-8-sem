# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить возможностью изменения и удаления данных 

import os

def DataOutput (Filename):
    data = open(Filename,'r',encoding ='utf-8')
    for line in data:
        print(line)
    data.close()

def WriteData (Filename):
    newrecord = str(input("Введите новую запись в формате (Фамилия Имя Отчество Телефон Пол)=> ")) + '\n'
    data = open(Filename,'a',encoding ='utf-8')
    data.writelines(newrecord)
    data.write('\n')
    data.close()

def Search_by_characteristic (Filename):
    characteristic = str(input("Укажите одну любую характеристику из списка (фамилия, имя, отчество, тел (10 цифр) или пол (муж, жен) => "))
    with open(Filename,'r',encoding ='utf-8') as data:
        for line in data:
            if str(characteristic).upper() in str(line).upper():
                print(line)

def Deletestring (Filename):
    with open(Filename,'r',encoding ='utf-8') as data:
        Recordsinput = data.readlines()
    deletestring = str(input("Укажите характеристику для строки, которую вы хотите удалить => "))
    Recordsoutput = []
    for i in range(0,len(Recordsinput)):
        if deletestring.upper() not in Recordsinput[i].upper():
            Recordsoutput.append(Recordsinput[i])
    with open(Filename,'w',encoding ='utf-8') as data:
        data.writelines(Recordsoutput)
                    
def Changestring (Filename):
    with open(Filename,'r',encoding ='utf-8') as data:
        Recordsinput = data.readlines()
    changestring = str(input("Укажите характеристику для строки, которую вы хотите изменить => "))
    newrecord = str(input("Введите новую редакцию строки, которую вы хотите поменять (Фамилия Имя Отчество телефон пол) => ")) + '\n'
    Recordsoutput = []
    for i in range(0,len(Recordsinput)):
        if changestring.upper() in Recordsinput[i].upper():
            Recordsoutput.append(newrecord)
        else:
            Recordsoutput.append(Recordsinput[i])
    with open(Filename,'w',encoding ='utf-8') as data:
        data.writelines(Recordsoutput)
                       
os.system('CLS')
print ("ТЕЛЕФОННЫЙ СПРАВОЧНИК")
print("Функционал: \n 1. Вывод данных из справочника \n 2. Добавление данных в справочник \n 3. Поиск записей по условию \n 4. Удаление данных \n 5. Изменение данных")
operation = int(input("Введите, что вы хотите сделать (1,2,3,4 или 5)=> "))
Filename = 'Data_file.txt'

if operation == 1:
    DataOutput(Filename)
elif operation == 2:
    WriteData(Filename)
elif operation == 3:
    Search_by_characteristic(Filename)
elif operation == 4:
    Deletestring (Filename)
elif operation == 5:
    Changestring (Filename)
    
else:
    print("Недопустимый ввод кода операции!")




















