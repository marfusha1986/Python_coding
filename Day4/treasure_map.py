row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

mp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to put the treasure? ")

horizontal = int(pos[0]) #2
vertical =int(pos[1])    #3

#selected_row = mp[vertical-1]
#selected_row[horizontal-1] = "X"

mp[vertical-1][horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")