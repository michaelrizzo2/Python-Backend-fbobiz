#First we need to import the request module

import requests

#Now we need to make a get request

r=requests.get("http://www.google.com")

#NOw we need to get the statuts of the webpage
print (r.status_code)
#A status code of 200 means the request has been successful
print (r.headers['content-type'])
#We get that the content is html code
