import json

x = '{"name":"alex", "age":120, "job":"developer"}'
y = json.loads(x)


print(y)