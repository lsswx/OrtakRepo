#Hocam selamun aleykum ben bu projede http://books.toscrape.com/index.html sitesinden tüm kitap adlarını çekmeye çalışdım fakat sadece katagori sınıflarına göre veri çekiyor . 
#ben bu projede siteden tüm kitap adlarını ve fiyatlarını nasıl çekebilirim ? Veriyi çekdikten program otomatik olarak bunu excele kopyalayabilirmi ? şimdiden teşekkürler .

# In[32]:


from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 
  
merhabaurl = 'http://books.toscrape.com/index.html'
uClient = uReq(merhabaurl) 
page_html = uClient.read() 
uClient.close() 
page_soup = soup(page_html, "html.parser") 
bookshelf = page_soup.findAll( 
    "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"}) 
filename = ("Books.csv") 
f = open(filename, "w") 
  
headers = "Book title,  Price\n\n"
f.write(headers) 
  
for books in bookshelf: 
    book_title = books.h3.a["title"] 
    book_price = books.findAll("p", {"class": "price_color"}) 
    price = book_price[0].text.strip() 
  
    print("Kitabın adı:" + book_title) 
    print("Kitabın fiyatı:" + price) 
  
    f.write(book_title + "," + price+"\n\n") 
f.close() 


# In[ ]:




