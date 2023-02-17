dictionary = {"one": "two", "two": "three", "three": "one"}
v = dictionary["one"]
for k in range(len(dictionary)):
    print(v)
    v = dictionary[v]
print(v)