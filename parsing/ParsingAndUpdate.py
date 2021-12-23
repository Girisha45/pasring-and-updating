import json
# parsing a json file
a_file = open("data.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)

# updating the value

json_object["d"] = 100

a_file = open("sample_file.json", "w")
json.dump(json_object, a_file)
print(json_object)
a_file.close()