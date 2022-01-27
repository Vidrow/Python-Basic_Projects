import re
import pyperclip


# Creating phone number Regex
# considering indina number

phonenum_regex = re.compile('''
                            [0-9]{3}    #First three digits
                            -          #hyphen
                            [0-9]{7}   #Last seven digits

''', re.VERBOSE)

# Creating Email Regex

email_regex = re.compile(r'''
                              [a-zA-Z0-9.-]+      #Username
                              @                   # @ symbol
                              [a-zA-Z.a]+        #gmail or yahoo something
                              \.[a-z]{3}      #domain name

''', re.VERBOSE)


text = str(pyperclip.paste())


finding = []
for i in phonenum_regex.findall(text):
    finding.append(i)

for j in email_regex.findall(text):
    finding.append(j)

print(finding)
