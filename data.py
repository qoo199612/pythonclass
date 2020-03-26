# class Drink:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_name(self):
#         return self.__name


#--------------------------------------------
"""


class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):                 #用來限制輸入只能M或F
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print("=======請傳入正確性別=======")
    def borrow_resources(self):
        pass

    def join_class(self):
        pass
    def quit_class(self):
        pass

class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('student borrow')

    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resources(self):
        print('student borrow')

class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print('professor borrow')
studentA = Student('M', '工管系', 'M10821005')
studentB = Student('F', '美術系', 'M10821007')
professorC = Professor('F', '戲劇系', 'M10821009')
professorD = Professor('M', '財稅系', 'M108210011')

ls = [studentA, studentB, professorC, professorD]

for item in ls:
    item.borrow_resources()
"""

class Pokemon:
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        self.__name = new_name
        self.__weight = new_weight
        self.__height = new_height
        self.__food = new_food
        self.__cp = new_cp

    def get_eat(self):
        print(f"The pokemon is eating {self.__food}.")
    def get_make_noice(self):
        print("The pokemon wow wow wow!")
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self,__name = new_name
    def get_weight(self):
        return self.__weight
    def set_weight(self, new_weight):
        self, __weight = new_weight
    def get_height(self):
        return self.__height
    def set_height(self, new_height):
        self, __height = new_height
    def get_food(self):
        return self.__food
    def set_food(self, new_food):
        self, __food = new_food
    def get_cp(self):
        return self.__cp
    def set_cp(self, new_cp):
        self, __cp = new_cp
class Pikachu(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        self.__name = new_name
        self.__weight = new_weight
        self.__height = new_height
        self.__food = new_food
        self.__cp = new_cp
    def get_eat(self):
        print(f"{self.get_name()} is eating {self.get_food()}.pika")
    def get_make_noice(self):
        print(f"{self.__name} pika pika chu!")

class Squirtle(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        self.__name = new_name
        self.__weight = new_weight
        self.__height = new_height
        self.__food = new_food
        self.__cp = new_cp
    def get_eat(self):
        print(f"{self.get_name()} is eating {self.get_food()}.jenny jenny")
    def get_make_noice(self):
        print(f"{self.__name} jenny jenny!")

Pokemon1 = Pikachu('國禎', 90, 2, '大便', 0)
Pokemon1 = Pikachu('國禎', 90, 2, '大便', 0)
