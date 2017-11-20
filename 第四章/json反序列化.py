import json

f = open('test.txt', 'r')
# data = eval(f.read())
data = json.loads(f.read())
print(data['age'])
f.close()
# print(data['age'])
