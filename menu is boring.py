def menu_is_boring(meals):
    for i in meals:
        if meals.count(i) > 1:
            return True
    return False

meals = ["Spam","Bag","Bag"]
print(menu_is_boring(meals))
