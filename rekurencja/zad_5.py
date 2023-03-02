def silna_iteration(x:int):
    solution = x
    while x>1:
        x = x-1
        solution *= x
    return solution

for x in range(7):
    print(x)
    print(silna_iteration(x))
    print()