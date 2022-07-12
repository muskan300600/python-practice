def fact(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

def func_recursion(n):
    for i in range(n):
        if n==1 or n==0:
            return 1
        return func_recursion(n-1)*n

print(func_recursion(5))

