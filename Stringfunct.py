
def func(str,word):
  newstr=str.replace(word,"")
  return newstr.strip()

str="      Mini is a good girl      "
n=func(str, "Mini")
print(n)
