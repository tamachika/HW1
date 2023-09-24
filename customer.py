class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name  
        self.age = age  
    
    def entry_fee(self):
        if self.age < 3:
            print(0)
        if 3 < self.age < 20:
            print(1000)
        if 20 < self.age < 65:
            print(1500)
        if 65 <= self.age <= 75:
            print(1200)
        if 75 < self.age:
            print(500)

    def info_csv(self):
        list = [self.first_name, self.family_name, self.age, self.entry_fee()]
        print("|".join(map(str, list)))#ここを変更すればC4,7,8に対応できる

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


"""
#c1
class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name  
        
    def full_name(self):
        print(self.first_name +" "+ self.family_name )
        
ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す


#c2
class Customer:
    def __init__(self, first_name, family_name, age):
        print(self.age)

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す

#c4
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name  
        self.age = age  
    
    def entry_fee(self):
        if self.age < 3:
            print(0)
        if 3 < self.age < 20:
            print(1000)
        if 20 < self.age < 65:
            print(1500)
        if 65 <= self.age <= 75:
            print(1200)
        if 75 < self.age:
            print(500)

    def info_csv(self):
        list = [self.first_name + " " + self.family_name, self.age, self.entry_fee()]
        print(",".join(map(str, list)))
        #ここを変更すればC7,8に対応できる

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


"""