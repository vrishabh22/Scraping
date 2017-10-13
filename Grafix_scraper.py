from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
url='https://www.newegg.com/Headphones/Category/ID-158?Tpk=headphones'
#download page
uCli=req(url)#open connection
page_html=uCli.read()#read page html
uCli.close()#close connection

page_soup=soup(page_html,'html.parser')#page_soup.h1 , page_soup.p etc

fname='products.csv'
f=open(fname,'w')
header="BRAND,PRODUCT_NAME,SHIPPING\n"
f.write(header)

#Products
containers=page_soup.find_all("div",{"class":"item-container"})
for container in containers:
    #brand name
    #brand=container.div.div.a.img["alt"]


    #name
    title_cont=container.find_all("a",{"class":"item-title"})
    name=title_cont[0].text
    brand=name.split(' ', 1)[0]
    #shipping
    ship_cont=container.find_all("li",{"class":"price-ship"})
    detail=ship_cont[0].text.strip()
    f.write(brand + "," + name.replace(",","|") + "," + detail)
    f.write("\n")

f.close()