import json

try:
    contacts = {}
    name = str(input("Enter name: "))
    phone = int(input("Enter phone number: "))

    if not name or not phone:
        raise ValueError("Name and phone number cannot be blank.")

    contacts[name] = phone

    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

    with open("contacts.json", "r") as f:
        data = json.load(f)

    print(data)

    if name in data:
        print("Contact found:", name)
    else:
        print("Contact not found.")

except json.JSONDecodeError:
    print("Error decoding JSON. Please check the file content.")
except ValueError as e:
    print("Invalid input Try again",e)
except KeyError:
    print("Key error occurred. Please check the data structure.")
except PermissionError:
    print("Permission error occurred. Please check file permissions.")
except TypeError:
    print("Type error occurred. Please check the data types.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("An error occurred:", e)
else:
    print("Contact saved successfully.")
finally:
    print("Execution completed.")
