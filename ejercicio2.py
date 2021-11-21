#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

# empiezo la sesion
session = requests.Session()

# creo el payload
payload = {'_username':'[YOUR_USERNAME]', 
          '_password':'[YOUR_PASSWORD]'
         }

# posteo el payload al sitio para logear
s = session.post("https://www.chess.com/login_check", data=payload)

# navego a la siguiente pagina y scrapeo los datos
s = session.get('https://www.chess.com/today')

soup = BeautifulSoup(s.text, 'html.parser')
soup.find('img')['src']


# In[2]:


import requests
from bs4 import BeautifulSoup

URL = "https://www.chess.com//"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

