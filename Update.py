import requests
import os
from bs4 import BeautifulSoup
mods = ['itemscroller','litematica','malilib','minihud','tweakeroo']
for i in mods:
    os.system("erase " + i + "*")
url = "https://masa.dy.fi/mcmods/client_mods/?mcver=1.15.2"
r = requests.get(url)
data = r.text
bs = BeautifulSoup(data, "html.parser")
link_list = bs.find_all("a",text="Download")

for urls in link_list:
    d = requests.get(urls['href'])
    name = urls['href'][urls['href'].rfind("/")+1:]
    print(name)
    with open(name, "wb") as f:
        f.write(d.content)
