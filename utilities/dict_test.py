test = {"a":[1,2],"b":2,"c":3}
test2 = {"z":3,"x":2,"c":1}
print test2.keys()
print test.values()
print test2.keys() == test.keys()
for x in test:
    print x

test["a"].append(1)
print test.values()