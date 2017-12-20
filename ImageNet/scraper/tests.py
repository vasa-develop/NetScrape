from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')

import os
import threading
import requests

global lock

def get_image(link):
	lock = False
	os.system("wget "+link)
	lock = True

def download(soup):
	lock = True
	for a in soup.findAll('img'):
		if(lock == True):
			get_image(a['src'])

class scrape():
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self,soup):
        download(soup)


query = input("Image item: ")


for i in range(0, 101, 20):
    url = "http://images.google.com/search?q=" + query + "&sout=1&tbm=isch&ei=cpQuWtrOKcnMvgSNtbzICA&start=" + str(
        i) + "&sa=N"

    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    thread1 = scrape()
    thread1.run(soup)

#thread.start_new_thread(download, (soup,));



