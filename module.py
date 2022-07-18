x= input("Integer 1:")
y= input("Integer 2:")

try:
    z= (x) / int (y)
except Exception as e:
    print("Exception occurred: ",e)
    z= None
except Exception as e:
    print("Exception occurred: ",e)
    z= None
print("Division is: ",z)