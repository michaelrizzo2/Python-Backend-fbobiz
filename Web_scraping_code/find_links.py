#First we import beautiful soup
from bs4 import BeautifulSoup
#Next we need to import urllib
from urllib.request import urlopen

#Now we need to open the url
website_file=urlopen("http://www.reddit.com")

#Now we need to read the content from  the html file
website_html=website_file.read()

#Now we need to close the url
website_file.close()

#Now we need to scrape the links 
my_soup=BeautifulSoup(website_html,"lxml")

#This will find all of the links
my_links=my_soup.findAll("href")

for href in my_links:
    print("The link is {0}\n".format(href))
