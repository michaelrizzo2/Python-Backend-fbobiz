#we need to import the requests module to make a post request
import requests as req
#we need to get the values that we need to post to the website
values={"firstname":"abc","lastname":"xyz"}
#Now we need to post the data to the website
r=req.post("https://www.example.com",data=values)
print(r)
#Response successful http code of 200
