#first we need to import re
import re

my_string="3.14159278347435846584384658426785634863485763485634593468743"
a=re.findall("459",my_string)
print("The value is {0}".format(a))
b=re.findall("7",my_string)
print("The value is {0}".format(b))
