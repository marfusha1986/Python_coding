from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Bulbasaur","Ivysaur","Venusaur","Charmander"])
table.add_column("Type",["Normal","Fire","Grass","Electric"])
table.align ="l"

print(table)