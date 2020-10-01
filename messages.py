import requests
import mercari
import config
import settings

MAILGUN_API_KEY = settings.MAILGUN_API_KEY


key = MAILGUN_API_KEY
sandbox = 'sandbox554e088ba7b8498fa726f86f21885585.mailgun.org'
recipient = 'test@debsmail.com'


def send_email():
  request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
  request = requests.post(request_url, auth=('api', key), 
  data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Mercari Recent Skateboard Listings',
    'text': "Here is the most recent skateboard listings from Mercari  " +  mercari.current_listings
})

# mercari-skateboard-listings@sandboxef2056de0f3b4997bcde3014da144623.mailgun.org

# r = requests.post(
#   "",

#   auth=("api", "2e76d9c45315d248be855f62c8621c8d-aff2d1b9-fc983ab0"),

#   data={"from": 'hello@example.com',
#   "to": ["mercari-skateboard-listings@sandboxef2056de0f3b4997bcde3014da144623.mailgun.org"],
#   "subject": "test test test",
#   "text": "wu tang killa bees"
#   }
# )