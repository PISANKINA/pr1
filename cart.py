from ean import*
class Tovar:
    def __init__(self,name,charact,id_tov,
                 seria,year,price,uni_int,nalichie=True):
        self.__name=name
        self.__charact=charact
        self.id_tov=id_tov
        self.seria=seria
        self.year=year
        self.price=price
        self.uni_int=uni_int
        self.made="Страна-изготовитель зашифрована в уникоде"
        
        
    def __str__(self):
        s="Наименование товара "+self.__name+" "+"\n"
        s+="Характеристика: "+self.__charact+" "+"\n"
        s+="Id товара: "+self.id_tov+"\n"
        s+="Серия: "+self.seria+" "+"год выпуска: "+self.year+"\n"
        s+="Уникод:"+self.uni_int+"\n"
        s+="Страна изготовитель: "+self.made+"\n"
        s+="Цена: "+self.price+"\n"
        
        s+="\n"
        
        return s
    
    
    def __repr__(self):
        return self.__str__()
    
    def change_country(self):
        #print(d)
        if self.uni_int[0:3] in d.keys():
            print("По штрих-коду, страна-производитель: ", d[str(self.uni_int[0:3])])
        else:
            print("Страна-производитель не определена")



    def set_name(self, name):#изменить название товара
          self.__name = name


    def  get_name(self):#показать назваание товара
          return self.__name
    
    #@property #разрешает чтение свойства
    #def made(self):
        #return self.__made
    #@made.setter
    #def made_in(self,new_country):
        
        #self.__made=new_country


    def change_price(self,price):
        self.__change(price)


    def __change(self,price):
        self.price=price

class Bag:
    def __init__(self,person,charact,copasity,tovars):
        self.person=person
        self.charact=charact
        self.copasity=copasity
        self.tovars=tovars
    def __str__(self):
        s2="Корзина принадлежит: "+self.person+"\n"
        s2+="Характеристика: " +self.charact+"\n"
        s2+="Вместимость: "+self.copasity+"\n"
        s2+="Товары в корзине:\n\n"+self.tovars
        return s2
    def __repr__(self):
        return self.__str__()
