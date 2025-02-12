!pip install bs4
from bs4 import BeautifulSoup
import requests as req
import pandas as pd
r=req.get("https://realpython.com/")
s=BeautifulSoup(r.text,"html.parser")
t=s.find_all("h2","card-title")
titles=[]
for i in t:
    titles.append(i.text)
dic={}
dic.update({"Titles":titles})
data=pd.DataFrame(dic)
print(data)
data.index=range(1,len(data)+1)
data.to_csv("cards_titles.csv")
