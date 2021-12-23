import json

myjsonfile=open("C:/Users/GIRISH/PycharmProjects/parsing/Employee.json",'r')
jsondata=myjsonfile.read()

# parse a file

object=json.loads(jsondata)

print(str(object['firstname']))
print(str(object['lastname']))

list=object['address']
print(list)
print(list[0])
print(list[1])
print(len(list))

for i in range(len(list)) :
    print("address of  ",i ," is ")
    print("street :",list[i].get("street"))
    print("city :",list[i].get("city"))
    print("state :",list[i].get("state"))





# # emp={"pin":561203}

# empdetails=json.loads(myjsonfile)
#
# empdetails.update(emp)
#
# print(json.dumps(empdetails))


