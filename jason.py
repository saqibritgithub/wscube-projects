import json
#converting dictionaray into jason format
d={
    "name":"saqib moon",
    "course":"python",
     "fees":15000
}
s=[{ "name":"saqib moon",
    "course":"python",
     "fees":15000}]
z=json.dumps(s)
print(z)
print(type(z))
f=json.dumps(d)
print(f)
print(type(f))
#jason.loads (to convert json into data types)
d='{"name":"saqib","coursse":"python"}'
f=json.loads(d)
print(f)
print(type(f))
file=open("post.json","r")
x=file.read()
finaldata=json.loads(x)
print(finaldata)