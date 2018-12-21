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

#3.extract data
li_list = ul.find_all("li") #la mot list chua nhieu soup con vi no la san pham cua find_all
# print(li_list)
# for li in li_list:
#     print(li.prettify())
# print(ul.prettify())
# print(soup.prettify())
news_list = []
for li in li_list:
 a = li.h4.a
 title = a.string
 
 link = url + a["href"]
 

 news = OrderedDict({
     "title": title,
     "link":  link,
 })
 news_list.append(news)
#  print(news)
#  print("-----------------")
print(news_list)

pyexcel.save_as(records=news_list, dest_file_name="dantri1.xlsx")

    

# print(a)

# #2.extract ROI


# #3.extract data

# #4.save data to excel