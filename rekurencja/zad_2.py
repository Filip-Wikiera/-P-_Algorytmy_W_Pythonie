def print_binary(x:int):
    if x != 0:
        print_binary(int(x/2))
        print(x%2, end="")

table = [4,1,8,15,31,65,130]

for number in table:
    print(number)
    print_binary(number)
    print("\n"+"-"*30)