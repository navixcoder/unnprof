import re
try:
    with open("fintechDoc.txt","r") as f:
        email_pattern = r'[\w\.]+@[a-z]+\.''[a-z]+'
        num_pattern = r"\+\d{2}\s\d{5}\s\d{5}|\+\d{2}-\d{5}-\d{5}|\d{4}-\d{3}-\d{4}"
        Date_pattern = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}"
        Data=(f.read())
        print("-------------------TEXT INFORMATION EXTRACTION ---------------------")
        emails = re.findall(email_pattern,Data)
        print("EMAILS:")
        for email in emails:
            print(email)
        numbers = re.findall(num_pattern,Data)
        print("PHONE NUMBER:")
        for number in numbers:
            print(number)
        dates = re.findall(Date_pattern,Data)
        print("DATES:")
        for date in dates:
            print(date)
        print("----------------------------------------------")

except FileNotFoundError :
    print('file does not Exists')
except NameError:
    print("variable doesnt exists")
except Exception as e :
    print(e)


