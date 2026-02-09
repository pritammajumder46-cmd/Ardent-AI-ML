# PASSWORD STRENGTH CHECKER

import re # re -> Regular Expression

password = 'Hq@'
if re.search('[0-9]', password):
    print("Password has a anumber")
else:
    print("Weak Password")