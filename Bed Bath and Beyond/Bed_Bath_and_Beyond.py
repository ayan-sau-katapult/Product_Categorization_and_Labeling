import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://www.bedbathandbeyond.com/store/category/bedding/comforter-sets/15502?icid=L1_bedding_catmod_c025_22390_5_comfortersets&removeInStock=true"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'lxml')

tags=[]
for i in soup.findAll("div"):
    if i.a!=None:
        tags.append(i.a)

prod_list=[]
for i in tags:
    prod_list.append(i.text)

for i in list(set(prod_list)):
    if 'reviews' in i or 'room' in i or 'sign in' in i or 'buy' in i or 'Track' in i or i.isdigit() or 'deals' in i or 'buy' in i or 'occasion' in i or i=='Help' or i=="Shop now" or i=='':
        final_list.remove(i)
    else:
        continue

print(final_list)