from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content,"html.parser")


div = soup.find("div","cf_ResearchDataHistoryInfo")
table = div.find("table", id="tableContent")

tr_list = table.find_all("tr")

news_list = []
for tr in tr_list:
    td_list = tr.find_all("td","b_r_c")
    for td in td_list:
        a = td.string
        new = {
            "Thongtin": a,
        }
        news_list.append(new)
pyexcel.save_as(records=news_list,dest_file_name="thongtin.xlsx")




