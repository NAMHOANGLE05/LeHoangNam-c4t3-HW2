# food1 = "Egg"
# food2 = "Bun dau mam tom"
# food3 = "So huyet"
# food4 = "Rau sach"
# food5 = "Pho"




# menu = []_Empty list
# print(menu)
# print(type(menu))

# menu = ["Trung"]# List with one element
# print(*menu)

#
# menu = ["Trung", "Rau xanh", "Pho"]  # List with more than one element #read
# print(*menu, sep=", ")  # sep la viet tat cua separate
# menu.append("Bun dau")  # create
# print(*menu, sep=", ")
# menu.insert(0, "So huyet")
# print(*menu, sep=", ")



# game = [ "Player", "Enemy"]
# print(*game, sep=", ")
#
# ten_enemy = input("nhap ten enemy:")
# game.append(ten_enemy)
# print(*game , sep=", ")
#
# for _ in range(2):
#     Shoot_or_spawn = input("Nhap shoot hoac spawn:")
#     if Shoot_or_spawn.lower() == "shoot":
#         game.append("Bullet")
#     elif Shoot_or_spawn.lower() == "spawn":
#         game.append("Enemy")
#     print(*game ,sep=", ")

menu = ["Trung", "Rau xanh", "Pho" ]
# n = 1
# for food in menu:
#     print(n, food, sep = ". ")
#     n += 1 # viet tat cua n=n+1

# print(menu[0]) #-1 luon luon chi vao phan tu cuoi cung, dem tu so 0 Vd : 0,1,2,3
# menu[0] = "Trung trang"
#
# i = int(input("Enter position: "))-1 # do nguoi dem tu 1 , may dem tu 0
# new_food = input("Enter replacing food:")
# menu[i]= new_food
# print (menu[i])
# print (*menu, sep=", ")

# print(menu)
#
# # menu.pop(0) #remove
# # menu.remove("Pho")
#
# print(menu)

# for enumerate
for index, food in enumerate(menu):
    print(index + 1, food, sep = ", ")



