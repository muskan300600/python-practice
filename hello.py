letter = '''Dear <|NAME|>,
You are Selected.

Date: <|DATE|>'''

name=input("Enter tha name/n")
date=input("Enter the date/n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
