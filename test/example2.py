__author__ = 'pretty moon'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000266zBEAQ')
#assert 'Yahoo' in browser.title

elem = browser.find_elements_by_class_name("hidden-phone") # Find
print(elem)
#browser.quit()