#coding: UTF-8
from requests_oauthlib import OAuth1Session
from datetime import datetime
import settings

def lambda_handler(event, context):
    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    params = {"status": "テストツイートしてるぞー(" + datetime.now().strftime("%H:%M:%S") + ")"}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
    
    print('つぶやけたぞー')
    
    return {"statusCode": 200, "body": "つぶやけたぞー" }
