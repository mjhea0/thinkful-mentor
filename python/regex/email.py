import re

email_list = ["my@email.com", "@email.com", "my@email"]

pattern = "^[A-Za-z0-9.]+@[A-Za-z0-9.]+.com$"

for email in email_list:
    test = re.findall(pattern, email)    
    print test
