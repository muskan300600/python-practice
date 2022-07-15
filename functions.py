def sum(exp):
    total =0
    for item in exp:
        total=total+item
    return total

a= (567,937,839,749,77,33,284,9265,899,283,88,8,993,83,900,783,824,657,87, 7585,37,357,234,876)
b= (648,939,837,848,9393,9303,56,82,600,733,846,8,7384,86,456,3563,94,36584,3576,88,398,9837,8532)

a_sum = sum(a)
b_sum = sum(b)

print("A's total is:" , a_sum)
print("B's total is:", b_sum)


