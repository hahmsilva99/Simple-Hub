import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align:center;'>Web Scraper</h1>",unsafe_allow_html=True)
with st.form("search"):
    keyword=st.text_input("Enter your keyword")
    search=st.form_submit_button("search")
    if search:
        col1,col2=st.columns(2)
        page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup=BeautifulSoup(page.content,'lxml')
        rows=soup.find_all("div",class_="bugb2")
        for row in rows:
            figures=row.find_all("figure")
            for i in range(2):
                img=figures[i].find("img",class_="SpgDA")
                list=(img["srcset"].split("?"))
                if i==0:
                    col1.image(list[0])
                else:
                    col2.image(list[0])
                