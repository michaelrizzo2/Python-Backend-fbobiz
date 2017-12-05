#beautifulsoup 4 import is bs4
from bs4 import BeautifulSoup
#This is where we will import urllib 
from urllib.request import urlopen
#Now we need to set the url(urllib3 is urllib)
url=urlopen("http://www.python.org")
#Now we need to rean all of the content from the url
content=url.read()
#Next we need to have beautiful soup open up the url to look through everything 
#on the website
soup=BeautifulSoup(content,"lxml")
#Next we need to find all of the links on the web page
links=soup.findAll("a")

#Now we will save all of the python links to a file
my_file=open("links.txt","w")
for i in links:
    my_file.write("{0}\n".format(str(i)))
    print("writing {0}".format(i))

my_file.close()
