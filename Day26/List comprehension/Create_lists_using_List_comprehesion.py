import pandas


number = [1,2,3]
new_number = [n + 1 for n in number]

name = 'Angela'
letters_list = [letter for letter in name]
print(letters_list)

range(1,5)
doubled_num = [num * 2 for num in range(1,5)]
print(doubled_num)

names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [ name.upper() for name in names if len(name) >= 5]
print(short_names,long_names)