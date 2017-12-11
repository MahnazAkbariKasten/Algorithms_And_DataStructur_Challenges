__author__ = 'prettymoon'

from bs4 import BeautifulSoup
import re
import urllib

url = r"C:\Mahnaz\PycharmProjects\testCell\BC20160928.html"
page = open(url)
soup = BeautifulSoup(page.read())

print(soup.prettify())