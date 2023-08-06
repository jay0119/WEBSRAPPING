import requests
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import logging

flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"

urlclint = urlopen(flipcart_url)

flipcart_url = urlclint.read()

flipcart_html= bs(flipcart_url,'html.parser')

bigboxes = flipcart_html.findAll("div",{"class":"_1AtVbE col-12-12"})
print(len(bigboxes))
del bigboxes[0:2]
del bigboxes[-3:]

# for i in range(len(bigbox)):
#     print(bigbox[i].div.div.div.a['href'])

print(len(bigboxes))
box = bigboxes[len(bigboxes)-1]
product_link = "https://flipkart.com" + bigboxes[1].div.div.div.a['href']
print(product_link)
product_req = requests.get(product_link)
product_html = bs(product_req.text, 'html.parser')
product_boxes = product_html.findAll("div", {"class": "_16PBlm"})
print(len(product_boxes))
del(product_boxes[-1])
allReviews =[]
for i in product_boxes:
    print("Reviewer Name :")
    print(i.div.div.find('p',{"class":"_2sc7ZR"}).text)
    print("Reviewer Rating :")
    print(i.div.div.div.div.text)
    print("Reviewer Comment :")
    print(i.div.div.div.p.text)
    print("Reviewer Description :")
    print(i.div.div.find_all('div', {"class":""}))
    print("==================")
    review = {
        "name" : i.div.div.find('p',{"class":"_2sc7ZR"}).text,
        "rating" : i.div.div.div.div.text,
        "comment" : i.div.div.div.p.text,
        "description" : i.div.div.find_all('div', {"class":""})
    }
    allReviews.append(review)
print(allReviews)