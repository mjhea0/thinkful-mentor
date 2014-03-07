import re

phone_list = ["555-555-5555","555 555 5555","555.555.5555",
    "(555) 555-5555","(555)555-5555","(555)555.5555"]

pattern = r'\D'

for phone in phone_list:
    phone_num = re.sub(pattern, "", phone)    
    print "Phone Num : ", phone_num
