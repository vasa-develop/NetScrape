from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader , RequestContext
# Create your views here.

from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')
import urllib.request
import os
import threading
import requests
import random

def index(request):
    url = "http://images.google.com/search?q=girl&sout=1&tbm=isch&ei=cpQuWtrOKcnMvgSNtbzICA&start=0&sa=N"
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')


    for a in soup.findAll('img'):
        name = random.randrange(1, 1000)
        full_name = str(name) + ".jpeg"
        urllib.request.urlretrieve(a['src'],full_name)

    return HttpResponse("downloaded")


def imagescraper(request):
    template = loader.get_template('imagescraper/index.html')

    return HttpResponse(template.render())
