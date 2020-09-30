from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import requests
import lxml
from bs4 import BeautifulSoup
# import config

#give driver options to not display browser when running
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

##currently written to get latest skateboard listings from mercari

#add driver to chrome
driver = webdriver.Chrome(options=options)

#fetch website
driver.get('https://www.mercari.com/jp/')

#get input textbox
search_bar = driver.find_element_by_xpath('//*[@id="__next"]/div/header/div/div[1]/form/input')

sleep(2)

#enter text
search_bar.send_keys('スケートボード')

sleep(1)

#press enter key after input field is filled
search_bar.submit()

#select latest listings option from dropdown
driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/form/div[1]/div/div/select/option[4]").click()

          
#click not sold filter
not_sold = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/form/div[2]/div[8]/div/div[2]')

not_sold.click()

sleep(2)

#kanrio filter completion click
completion_button = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/form/div[2]/div[10]/button').click()


#get html values of page
driver.page_source


#get current listings
current_listings = driver.current_url

#print them
print(driver.current_url)


#api keys
# key = MAILGUN_
# sandbox = 'sandbox554e088ba7b8498fa726f86f21885585.mailgun.org'
# recipient = 'mercari-skateboard-listing@sandbox554e088ba7b8498fa726f86f21885585.mailgun.org'


# def send_email():
#   request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
#   request = requests.post(request_url, auth=('api', key), 
#   data={
#     'from': 'hello@example.com',
#     'to': recipient,
#     'subject': 'Mercari Recent Skateboard Listings',
#     'text': "Here is the most recent skateboard listings from Mercari  " +  current_listings
# })

#send email test
# send_email()

#close driver
driver.close()








