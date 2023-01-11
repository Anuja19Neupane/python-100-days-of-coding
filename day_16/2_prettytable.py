from prettytable import PrettyTable
table = PrettyTable()
table.add_column("country", ["nepal", "india", "US"])
table.add_column("population", [30000000,
                 45000000000, 360000000])
# in order to align your text
table.align = "l"  # "l" le left align garxa
print(table)
