# class person():
#     def __init__(self):
#         self.first_name=''
#         self.last_name=''
#
#     def get_default(self):
#         print('person information')
#         print("first_name:",self.first_name)
#         print("last_name:",self.last_name)
#
# p=person()
# p.first_name='prerna'
# p.last_name='thakur'
# p.get_default()
#
# p1=person()
# p1.first_name='minakshi'
# p1.last_name='mourya'
# p1.get_default()
# from Basic.practice import amount
#
#
# class account():
#     def __init__(self):
#         self.bank_name=''
#         self.account_number=''
#         self.balance=0
#
#
#     def get_account(self):
#         print('bank_name:',self.bank_name)
#         print('account_number:',self.account_number)
#         print('balance:',self.balance)
#     #
#     def deposit(self,amount):
#         self.balance +=amount
#         print(amount,'deposit,update balance:',self.balance)
#
#     def withdraw(self,amount):
#         self.balance -=amount
#
#         print(amount,'withdrow,update balance:',self.balance)
# #
# a=account()
# a.bank_name='SBI'
# a.account_number='SBI22331155'
# a.balance=1000
#
# a.get_account()
# a.deposit(500)
# a.withdraw(200)
#
# class User():
#     count=0
#     def __init__(self):
#         self.first_name=''
#         self.last_name=''
#
#     def get_details(self):
#         print('first_name:',self.first_name)
#         print('last_name:',self.last_name)
#
#     @classmethod
#     def test_class_method(cls):
#         print('this is class method')
#
#     @staticmethod
#     def test_static_method():
#         print('this is static method')
#
# u=User()
# u.first_name='abc'
# u.last_name='xyz'
# u.get_details()
#
# print(User.count)
# User.test_class_method()
# User.test_static_method()

#
# class Car():
#     # speed=200
#     def __init__(self):
#         self.brand = ''
#         self.color = ''
#         self.speed = 0
#
#     def display_details(self):
#         print('brand:', self.brand)
#         print('color:', self.color)
#         print('speed:', self.speed)
#
#     @staticmethod
#     def calculate_distance():
#         print('distance :', '10 km')
#
#     @classmethod
#     def display_car_count(cls):
#         print('dispaly car count:', '15 car')
#
#
# a = Car()
# a.brand = 'BMW'
# a.color = 'black'
# a.speed = 100
# a.display_details()
# #
# # print(car.speed)
# Car.calculate_distance()
# Car.display_car_count()
