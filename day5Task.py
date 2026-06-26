import re
try:
    with open("fintechDoc.txt","r") as f:
        email_pattern = r"[a-zA-Z0-9_.]+@""[a-z.]+"
        number_pattern = r"[\d{0-9}]+""[+\d{2}-\d{5}-\d{5}+""\d{4}-\d{3}-\d{4}]+""[+\d{2} \d{3} \d{5}]"
        Data=(f.read())
        print(Data)
        emails = re.findall(email_pattern,Data)
        print(emails)
        phone_numbers = re.findall(number_pattern,Data)

except FileNotFoundError :
    print('file does not Exists')
except NameError:
    print("variable doesnt exists")
except Exception as e :
    print(e)

