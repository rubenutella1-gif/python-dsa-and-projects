#import section
import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_="KzDlHZ")
#print(names)
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)  
prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
#print(price)
ratings=soup.find_all('div',class_="XQDdHH")
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(float(d))
#print(rating)    
images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)    

data={"Names":name,
      "prices":price,
      "Ratings":rating,
      "Images":image}
# print(data)
df=pandas.DataFrame(data)
print(df)
df.to_csv("Mobile_data.csv")