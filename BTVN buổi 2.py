# A Boolean value is either true or false
#    Ex:     9 >= ( 2+1+2 )
#            9*2 == 6*3
#            6 % 2 == 0

# - Flowchard dung de dien ta qua trinh chạy của một Conditional Execution hay 1 hàm có condition ( if )
# - Nested condition là condition con của 1 condition khác Hay 1 hệ condition có nhiều condition nhỏ trong mỗi condition
# Ex: If Delta > 0:
#             Print( Phuong trinh co 2 no phan biet )
#             else:
#                     ìf Delta == 0:
#                         Print ( Phuong trinh co no kep )
#                             else:
#                                 Print ( Phuong trinh vo no )


# Ve turtle

# 1a
# from turtle import*
#
# left(120)
# forward (100)
# right(60)
# forward(100)
# right(120)
# forward(100)
# right(60)
# forward(100)
# forward(100)
# left(60)
# forward(100)
# left(120)
# forward(100)
# left(60)
# forward(100)
# right(150)
# forward(100)
# left(60)
# forward(100)
# left(120)
# forward(100)
# left(60)
# forward(100)
# forward(100)
# right(60)
# forward(100)
# right(120)
# forward(100)
# right(60)
# forward(100)
#
# mainloop()



# 1b
# from turtle import *
#
# for _ in range (3):
#     forward(100)
#     left(120)
# for _ in range (4):
#     forward (100)
#     left (90)
# for _ in range (5):
#     forward (100)
#     left (72)
# for _ in range (6):
#     forward (100)
#     left(60)
#
# mainloop()



# Serious excercise
# 1
# height = int( input (" Nhap height(cm) "))
# weight = int ( input (" Nhap weight(kg) "))
# H=height/100
# BMI =(weight)/(H*H)
# if BMI<16:
#     print ("You are severely underweight")
# if BMI>=16 and BMI<18.5:
#     print("You are underweight")
# if BMI>=18.5 and BMI<25:
#     print("You are normal")
# if BMI>=25 and BMI<30:
#     print("Overweight")
# if BMI>=30:
#     print('Obese')


# 2
# n = int( input ("Nhap so n "))
# Tich = 1
# for i in range (1,(n+1)) :
#     Tich = Tich*i
# print(Tich)


# 3
# a
# for i in range (1,21):
#     print(i, end = " ")

# n = int( input ("Nhap so n "))
# for i in range (1,(n))    :
#     print(i, end = " ")

# b
# for _ in range (11):
#     print(1,0 , end = " ")
#
# n = int( input("Nhap so n "))
# for i in range (1,(n+1)):
#     print(1,0 , end = " ")















# Session 2b
#  Net list is a list in a list
#  A list can have both integer and string in it


# 1
# from turtle import *
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
#
# for _ in range (3):
#     pencolor(colors[0])
#     forward(100)
#     left(120)
# for _ in range (4):
#     pencolor(colors[1])
#     forward (100)
#     left (90)
# for _ in range (5):
#     pencolor(colors[2])
#     forward (100)
#     left (72)
# for _ in range (6):
#     pencolor(colors[3])
#     forward (100)
#     left(60)
# for _ in range (7):
#     pencolor(colors[4])
#     forward(100)
#     left(51.4)
#
# mainloop()


#2
# from turtle import*
#
# speed(-1)
#
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# left(90)
# for _ in range (20):
#     pencolor(colors[0])
#     forward(100)
#     right(90)
#     forward(1)
#     right(90)
#     forward(100)
#     left(90)
#     forward(1)
#     left(90)
# for _ in range (20):
#     pencolor(colors[1])
#     forward(100)
#     right(90)
#     forward(1)
#     right(90)
#     forward(100)
#     left(90)
#     forward(1)
#     left(90)
# for _ in range (20):
#     pencolor(colors[2])
#     forward(100)
#     right(90)
#     forward(1)
#     right(90)
#     forward(100)
#     left(90)
#     forward(1)
#     left(90)
# for _ in range (20):
#     pencolor(colors[3])
#     forward(100)
#     right(90)
#     forward(1)
#     right(90)
#     forward(100)
#     left(90)
#     forward(1)
#     left(90)
# for _ in range (20):
#     pencolor(colors[4])
#     forward(100)
#     right(90)
#     forward(1)
#     right(90)
#     forward(100)
#     left(90)
#     forward(1)
#     left(90)
#
#
#
# mainloop()


# 1
# Our_items = ["T-shirt", "Sweater"]
# print ("Welcome to our shop, what do you want ( C, R, U, D)" )
# Customer = input("Input C/R/U/D ")
# if Customer.upper()=="R":
#     print(*Our_items, sep=", ")
# if Customer.upper()=="C":
#     New_items = input("Input new items ")
#     Our_items.append(New_items)
#     print(*Our_items, sep=", ")
# if Customer.upper()=="U":
#     Update_position = int( input ("Update position "))
#     New_items = input("Input new items ")
#     Our_items.insert(Update_position, New_items)
#     print(*Our_items, sep=", ")
# if Customer.upper()=="D":
#     Delete_position = int(input("Delete position "))
#     Our_items.remove(Our_items[Delete_position])
#     print(*Our_items, sep=", ")


# 2.1
# Name = input("Type your name ")
# print("Hello, my nam is ",Name, " and these are my sheep sizes")
#
# Sheep_sizes = []
# for _ in range (7):
#     Sizes = int (input ("Sizes of sheep "))
#     Sheep_sizes.append ( Sizes )
# print (*Sheep_sizes, sep = ", ")
#
# Biggest = max(Sheep_sizes)
# print("Now my biggest sheep has size ", Biggest, " let's shear it")
#
# Sheep_sizes.remove (Biggest)
# print("After sheering, hear is my flock")
# print ( *Sheep_sizes, sep = ", ")
#
#
#
#
# print("MONTH 1: ")
# print("One moth has passed, now here is my flock")
# for i in range (len(Sheep_sizes)):
#     Sheep_sizes[i] = Sheep_sizes[i] + 50
# print(*Sheep_sizes, sep = ", ")
#
# Biggest = max(Sheep_sizes)
# print("Now my biggest sheep has size ", Biggest, " let's shear it")
#
# Sheep_sizes.remove (Biggest)
# print("After sheering, hear is my flock")
# print ( *Sheep_sizes, sep = ", ")
#
#
#
#
#
# print("MONTH 2: ")
# print("One moth has passed, now here is my flock")
# for i in range (len(Sheep_sizes)):
#     Sheep_sizes[i] = Sheep_sizes[i] + 50
# print(*Sheep_sizes, sep = ", ")
#
# Biggest = max(Sheep_sizes)
# print("Now my biggest sheep has size ", Biggest, " let's shear it")
#
# Sheep_sizes.remove (Biggest)
# print("After sheering, hear is my flock")
# print ( *Sheep_sizes, sep = ", ")
#





# print("MONTH 3: ")
# print("One moth has passed, now here is my flock")
# for i in range (len(Sheep_sizes)):
#     Sheep_sizes[i] = Sheep_sizes[i] + 50
# print(*Sheep_sizes, sep = ", ")
#
# Biggest = max(Sheep_sizes)
# print("Now my biggest sheep has size ", Biggest, " let's shear it")
#
# Sheep_sizes.remove (Biggest)
# print("After sheering, hear is my flock")
# print ( *Sheep_sizes, sep = ", ")
#
#
# Total = 0
# for i in range (len(Sheep_sizes)):
#     Total = Total + Sheep_sizes[i-1]
# print("My flock has sizes in total: ", Total)
# Profit = Total * 2
# print("I would get ",Total, "* 2$ = ", Profit , " $ ")

# 3.1
# import random
# Word = [ "c", "h", "a", "m", "p", "i", "o", "n"]
# random.shuffle( Word )
# print (*Word, sep = ", ")
# User_answer = input("Your answer: ")
# if User_answer == "champion" :
#     print ( " Hura ")
# else:
#     print ( "Wrong answer")
#
#
#
# Word = [ "s", "t", "u", "d", "e", "n", "t", "s"]
# random.shuffle( Word )
# print(*Word, sep = ", ")
# User_answer = input("Your answer: ")
# if User_answer == "students" :
#     print ( " Hura ")
# else:
#     print ( "Wrong answer")
#
#
#
# Word = [ "t", "e", "c", "h", "k", "i", "d", "s"]
# random.shuffle( Word )
# print(*Word, sep = ", ")
# User_answer = input("Your answer: ")
# if User_answer == "techkids" :
#     print ( " Hura ")
# else:
#     print ( "Wrong answer")
















