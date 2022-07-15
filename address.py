book = {}
book["Tom"]={"name":"tom", "Address":"America","Phone":"1234"}
book["Dick"]={"name":"dick", "Address":"China","Phone":"1734"}
book["Harry"]={"name":"harry", "Address":"NY","Phone":"1904"}

import json
s=json.dumps(book)
print(s)