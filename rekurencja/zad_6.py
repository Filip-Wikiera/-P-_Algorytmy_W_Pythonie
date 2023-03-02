def binary_search(x:int,table):
    left = 0
    right = len(table) - 1
    while left <= right:
        mid = (right+left)//2
        if x == table[mid]:
            return mid
        elif x > table[mid]:
            left = mid+1
        else: right = mid-1

    return -1




table = [1,2,3,4,5,6,7,8]
table2 = []
table3 = [1,2,3,4,5,6,7]

for x in table:
    table2.append(x*4)
table2.append(1000)
x = 8
print(binary_search(x, table))
print(binary_search(x, table2))
print(binary_search(x, table3))