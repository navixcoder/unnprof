import json
contacts = {}
name=input("Enter name: ")
phone=input("Enter phone number: ")
contacts[name]=phone
with open("contacts.json","w") as f:
    json.dump(contacts,f)
with open("contacts.json","r") as f:
    data=json.load(f)
print(data)
if name in data:
    print("Contact found: ", name)
else:
    print("Contact not found.")