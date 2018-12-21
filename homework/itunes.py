from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read() #doc data
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content,"html.parser")

section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")
# print(li_list)

news_list = []
for li in li_list:
 a= li.h3.a
 b= li.h4.a
 song= a.string
 name= b.string



 new  = OrderedDict({
     "songs": song,
     "name": name,
 })
 news_list.append(new)

# save
pyexcel.save_as(records=news_list,dest_file_name="itunes.xlsx")

options = {
    "default_search": "ytsearch",
    "max_dowloads": 1 
}
dl = YoutubeDL(options)
dl.download([song +  name])


    
    





