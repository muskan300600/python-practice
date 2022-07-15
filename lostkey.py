keys=(23,45,65,45,67,56,12,98,90,9,567,937,94,789,927553,26453,99,77,365933,7454,7303)
key_location=9
#value=input("Enter your key:")
for x in keys:
    if x==key_location:
        print("Yay! key found and it is ",x)
        break
    else:
        continue