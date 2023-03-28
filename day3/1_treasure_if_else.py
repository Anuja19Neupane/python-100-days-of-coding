print("welcome to treasure island.")
print("your mission is to find the treasure.")
way = input(
    "you are at a cross road.where do you want to go? type left or right. ")
if way == "left":
    left = input(
        "you are now in a middle of lake. type'wait'to wait for a boat or type'swim'to go by yourself. ")
    if left == "wait":
        print("OOPS!you died because of drowning.")
    else:
        print("CONGRATS! you survived.")
else:
    right = input(
        "you are in the midddle of the jungle.Type 'walk'to move forward or 'sleep' to take rest. ")
    if right == "walk":
        print("CONGRATS!you survived.")
    else:
        print("OOPS!you became a prey of tiger.")
