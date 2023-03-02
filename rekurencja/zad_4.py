def greatest_common_divisor1(a:int,b:int):
    if b == 0:
        return a
    else:
       return greatest_common_divisor1(b,a%b)
def greatest_common_divisor2(a:int,b:int):
    if a==b:
        return a
    if a<b:
        a, b = b, a

    return greatest_common_divisor2(b,a-b)

a = 10
b = 15
print(greatest_common_divisor1(a,b))
print(greatest_common_divisor2(a,b))
