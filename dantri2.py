from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1.download trang
url = "https://dantri.com.vn"
#1.1 Open c connection to server
conn = urlopen(url)
#1.2 Read data
raw_data =  conn.read()
#1.3 Decodde data
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew") #id = "ul1 ulnew" 
print(ul)

#3.extract data
li_list = ul.find_all("li") #la mot list chua nhieu soup con vi no la san pham cua find_all

a = li_list[0].h4.a

print(a)

    