my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5,]
index = 0
while index < len(my_list[0::]):
    if my_list[index] < 0 :
        index +=1
        break
    print (my_list [index])
    index += 1
# Здравствуйте без 0 вывести не получается (((...


