indian=["Paratha","Dosa","Idli","Sabji"]
chinese=["Chowmein","Manchurian","Choupsey"]
italian=["Pizza","Fries","Pasta"]

Dish=input("Enter a dish")

if Dish in indian:
    print("Indian")
elif Dish in chinese:
    print("chinese")
elif Dish in italian:
    print("Italian")
else:
    print("Invalid dish")