def rise_to_power(x, n):
    if n == 0:
        return 1
    else: return x*rise_to_power(x, n-1)

def rise_to_power2(x, n, temp = 1):
    print(x)
    print(n)
    print(temp)
    print("-------")
    if n == 0:
        return temp
    else: return rise_to_power2(x, n-1, temp*x)



for x in range(10):
    print(x)
    print(rise_to_power(x,3))
    print(rise_to_power2(x, 3))
    print("-"*30)