import re
try:
    with open("fintechDoc.txt","r") as f:
        email_pattern = r'[\w\.]+@[a-z]+\.''[a-z]+'
        Data=(f.read())
        print(Data)
        emails = re.findall(email_pattern,Data)
        print(emails)

except FileNotFoundError :
    print('file does not Exists')
except NameError:
    print("variable doesnt exists")
except Exception as e :
    print(e)

