lis=["computer","monitor","keybord","mouse","mousepad","hdmi cable"]
current_choice = "_"
computer_parts = [] # createvan empty list
valid_choices=[str(i) for i in range(1,len(lis)+1)]
print (valid_choices)

while current_choice != "0" :
    if current_choice in valid_choices:
        
        index = int(current_choice)-1
        chosen_part = lis[index]
        if chosen_part in computer_parts:
            print("removing {} ".format(current_choice))
            computer_parts.remove(chosen_part) 
        else:
            print("Adding {} ".format(current_choice))
            computer_parts.append(chosen_part)     

        print("your list now contains: {}".format(computer_parts))               

    else:
        print("please add options from the list below: ")
        for number,part in enumerate(lis):
            print("{}: {}".format(number+1,part))
        print("0: to exit")   

    current_choice = input()

print(computer_parts)