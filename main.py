from cart import*
from ean import*
def main():
    a=[]
    file_in=open("file.txt","w")
    file_in.write("ТОВАРЫ:\n")
    file_in.write("\n")
    file_in.close()
    menu(a)
    return

def menu(a):
    x=0
    while x!=12:
        print("Меню")
        print("0.Создать корзину(сначала)")
        print("1.Добавить информацию о новом товаре")
        print("2.Посмотреть данные в списке(архиве)")
        print("3.Записать данные из списка в файл")
        print("4.Вывести названия всех товаров архива на экран")
        print("5.Изменить название товара из архива")
        print("6.Посмотреть данные в файле")
        print("7.Изменить цену товара(по очередности в списке)")
        print("8.Вывести информацию о корзине и товарах, которые в ней находяться")
        print("9.Удалить товар из корзины")
        print("10.Посмотреть словарь-расшифровку символов страны поставщика формата EAN-13")
        print("11.Расшифровать уникод, чтобы узнать страну поставщика")
        print("12.Выход")
        x=int(input())
        if x==0:
            person=input("Кому принадлежит корзина?  ")
            charact=input("Введите основные характеристики корзины: ")
            copasity=input("Максимальная сумма вмещения: ")
            t=""
            bag=Bag(person,charact,copasity,t)
            print(bag)
        if x==1:
            menu1(a)
            change(a,bag)
        if x==2:
            print(a)
        if x==3:
            file_in=open("file.txt","w")
            s=""
            for elem in a:
                elem=str(elem)
                s+=elem
                s+="\n"
            file_in.write(s)
            file_in.close()

        if x==4:
            for i in range(len(a)):
                print(a[i].get_name())
        if x==5:
            n=int(input("Введите номер товара, название которого вы хотите изменить(по очередности в списке): "))
            for i in range(1, len(a)+1):
                if n==i:
                    ns=input("Введите новое название товара:  ")
                    a[i-1].set_name(ns)
            change(a,bag)

            
        if x==6:
            file_in=open("file.txt","r")
            s=file_in.read()
            print(s)
            file_in.close()
        if x==8:
            #nn=int(input("Введите номер товара(его очередность),страну производителя нужно изменить"))
            #for i in range(1,len(a)+1):
                #if nn==i:
                    #new_country=input("Введите новое название страны-поставщика")
                    #a[i-1].made_in=new_country
            print(bag)

            
        if x==7:
            w=int(input("Введите номер товара(очередность) "))
            price=input("Введите новую цену товара ")
            for i in range(1,(len(a)+1)):
                if w==i:
                    a[i-1].change_price(price)
            change(a,bag)
        if x==9:
            n=int(input("Введите номер товара(очередность), который вы хотите удалить: "))
            #print(a)
            for i in range(len(a)):
                if n==(i+1):
                    a.pop(i)
                    #print(a)
            change(a,bag)
        if x==10:
            print(d)
            #a[0].change_country()
        if x==11:
            v=int(input("Введите номер товара в списке товаров,по очередности,начиная с первого"))
            for i in range(1,(len(a)+1)):
                if v==i:
                     a[i-1].change_country()
            change(a,bag)
def change(a,bag):
    t=""
    for elem in a:
        t+=str(elem)
    tovars=t  #"список" товаров
    
    bag.tovars=tovars
 
    return

#(self,name,charact,id_tov,seria,year,price,made="Russia", nalichie=True)
def menu1(a):
    
    print("Введите:")
    name=str(input("Название товара: "))
    charact=str(input("Характеристика: "))
    id_tov=str(input("Id товара: "))
    seria=str(input("Серия: "))
    
    year=str(input("Год: "))
    price=str(input("цена: "))
    #file_in=open("file.txt","a")
    uni_int=str(input("Введите штрих-код товара(13 цифр): "))
    tov=Tovar(name,charact,id_tov,seria,year,price,uni_int)
    a.append(tov)
    return a
main()

    
                
