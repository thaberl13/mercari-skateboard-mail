import requests
from flask import Flask, render_template, url_for, request
import os
# import mercari
# import config
import settings
MAILGUN_API_KEY = settings.MAILGUN_API_KEY

app = Flask(__name__)
app.config.update()


def subscribe_user(email, user_group_email, api_key):
  resp = requests.post(f"https://api.mailgun.net/v3/lists/{user_group_email}/members", 
  auth=("api", MAILGUN_API_KEY),
  data={"subscribed": True,
  "address": email}
  )

@app.route("/", methods=["GET", "POST"])
def index():

  if request.method == "POST":
    email = request.form.get('email')
    subscribe_user(email=email, user_group_email="mercari-skateboard-listing@sandbox554e088ba7b8498fa726f86f21885585.mailgun.org", api_key= MAILGUN_API_KEY)

  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)










