import json

info = {
  'name': 'alex',
  'age': 32
}
f = open('test.txt', 'w')
# f.write(str(info))
# print(json.dumps(info))
f.write(json.dumps(info))
f.close()
