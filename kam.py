# list =[1,2,3,4]
# tpl  = [10,26,45]
# list[1] = 100
# print(list)
# tpl[1] = 20
# print(tpl)
  
# def is_palindrome(s):
#       return s == s[::-1]
# print(is_palindrome("madam"))
# print(is_palindrome("church"))
# print(is_palindrome("mood"))

# def decorator_func(func):
#       def wrapper():
#             print("before function")
#             func()
#             print("after function")
#       return wrapper
# def say_hello():
#       print("hello!")
# say_hello()

# try:
#       x= 10 /0
# except ZeroDivisionError:
#       print("cannot divide by zero")
# finally:
#       print("done")

# from collections import Counter

# lst = [1,2,2,3,1,1]
# count = Counter(lst)
# print(count)

# class bankaccount:
#                def __init__(self,owner,balance=0):
#                        self.owner = owner
#                        self.__balance = balance
#                def deposit(self,amount):
#                        self.__balance += amount
#                        return self.__balance
#                def withdraw(self,amount):
#                        if amount>self.__balance:
#                                return "insufficient balance"
#                        else:
#                                self.__balance-=amount

#                                return self.__balance,self.owner
#                def get_bal(self):
#                        return  self.__balance
# acc = bankaccount("nirmala",9000)
# print(acc.deposit(7000))
# print(acc.withdraw(9000))
# print(acc.get_bal())

# def decorator(origunal_func):
#         def wrapper(*args,**kwargs):
#                 print("before  the function")
#                 origunal_func()
#                 print("after the function")
#         return wrapper
# @decorator
# def greet():
#         print("hello")
# greet()

# def count(n):
#         while n>0:
#                 yield n
#                 n-=1
# for num in count(8):
#         print(num)
# print(count(5))



# str = "nirmala bor"
# rev = ""
# for char in str:
#         rev = char+rev
# print(rev)

# a = {"x":1,"y":2}
# b = {"a":8,"b":8}
# merged = {**a,**b}
# print(merged)
# a.update(b)
# print(a)
# def fibo(n):
#         a,b = 0,1

# def dupli(lst):
#         uniq = list(set(lst))
#         return uniq
# print(dupli([2,3,4,4,3,2,3,4,55,6,54,4]))


# with open("copy.txt",'r')as file:
#         for line in file:
#                 print(line.strip())

# #how we remove duplicate wihtout using set 
# lst = [2,3,4,5,4,3,2,2,3,4,5,6,8]
# dupl = []
# seen = []
# for num in lst:
#         if num not in dupl:
#                 dupl.append(num)
#         else:
#                 seen.append(num)
# print(dupl)
# print(seen)
               

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)







