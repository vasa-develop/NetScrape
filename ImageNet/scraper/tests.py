from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')

import os
import threading
import requests


query = "girls"

url = "http://images.google.com/search?q=" + query + "&sout=1&tbm=isch&ei=cpQuWtrOKcnMvgSNtbzICA&start=0&sa=N"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

for a in soup.findAll('img'):
    os.system("wget " + a['src'])

#thread.start_new_thread(download, (soup,));



