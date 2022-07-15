numbers=[1,2,3,4,5,6,7,8,9,10]
even=[]
for x in numbers:
    if x%2==0:
        even.append(x)
    else: continue
print(even)

cities=["Mumbai","New York","Paris"]
countries=["India","America","France"]
z=zip(cities,countries)
d= {country:city for country, city in zip(countries, cities)}
print(d)