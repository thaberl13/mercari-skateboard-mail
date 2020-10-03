import requests
import mercari
import config
import settings
import schedule
import time



MAILGUN_API_KEY = settings.MAILGUN_API_KEY

sandbox = 'sandbox554e088ba7b8498fa726f86f21885585.mailgun.org'


def send_email():
  request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
  request = requests.post(request_url, auth=('api', MAILGUN_API_KEY), 
  data={
    'from': 'Mercari-skate-list@example.com',
    'to': 'thaberl13@gmail.com',
    'subject': 'Mercari Recent Skateboard Listings',
    'text': "Here are the most recent skateboard listings from Mercari:       " +  mercari.current_listings
})


send_email()

