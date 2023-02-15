def reverse_table(table, right, left = 0):
    if left < right:
        table[right], table[left] = table[left], table[right]
        reverse_table(table, right-1, left+1)


table_of_numbers = [1, 4, 5, 6, 12, 1406, 2137, 123]
print(table_of_numbers)
reverse_table(table_of_numbers, len(table_of_numbers)-1)
print(table_of_numbers)

