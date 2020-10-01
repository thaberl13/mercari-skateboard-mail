import requests
from flask import Flask, render_template, url_for, request
# import mercari
import config

app = Flask(__name__)


def subscribe_user(email, user_group_email, api_key):
  resp = requests.post(f"https://api.mailgun.net/v3/lists/{user_group_email}/members", 
  auth=("api", config.api_key or MAILGUN_API_KEY),
  data={"subscribed": True,
  "address": email}
  )

@app.route("/", methods=["GET", "POST"])
def index():

  if request.method == "POST":
    email = request.form.get('email')
    subscribe_user(email=email, user_group_email="mercari-skateboard-listing@sandbox554e088ba7b8498fa726f86f21885585.mailgun.org", api_key= config.api_key or MAILGUN_API_KEY)

  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)

# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandboxef2056de0f3b4997bcde3014da144623.mailgun.org/messages",
# 		auth=("api", "2e76d9c45315d248be855f62c8621c8d-aff2d1b9-fc983ab0"),
# 		data={"from": "Excited User <mailgun@sandboxef2056de0f3b4997bcde3014da144623.mailgun.org>",
# 			"to": ["yepoko@debsmail.com", "<mailgun@sandboxef2056de0f3b4997bcde3014da144623.mailgun.org>"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"}).status_code

# send_simple_message()
# requests.status_codes


# key = '2e76d9c45315d248be855f62c8621c8d-aff2d1b9-fc983ab0'
# sandbox = 'sandboxef2056de0f3b4997bcde3014da144623.mailgun.org'
# recipient = 'yepoko@debsmail.com'

# request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
# request = requests.post(request_url, auth=('api', key), data={
#     'from': 'hello@example.com',
#     'to': recipient,
#     'subject': 'misaki',
#     'text': "is cool"
# })

# mercari.current_listings

# print('Body:   {0}').format(request.text)




# key = '2e76d9c45315d248be855f62c8621c8d-aff2d1b9-fc983ab0'
# sandbox = 'sandboxef2056de0f3b4997bcde3014da144623.mailgun.org'
# recipient = 'yepoko2084@finxmail.net'

# request_url = 'https://api.mailgun.net/v3/sandboxef2056de0f3b4997bcde3014da144623.mailgun.org/messages'.format(sandbox)
# request = requests.post(request_url, auth=('api', key), data={
#     'from': 'hello@example.com',
#     'to': recipient,
#     'subject': 'Hello',
#     'text': 'Hello from Mailgun'
# })

# print('Status: {0}').format(request.status_code),
# print('Body:   {0}').format(request.text)
