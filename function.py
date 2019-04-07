#coding: UTF-8
import json
import hashlib
import hmac
from requests_oauthlib import OAuth1Session
from datetime import datetime
import settings

def lambda_handler(event, context):
    # HMAC値による簡易認証処理
    signature = event['headers']['X-Hub-Signature']
    signedBody = "sha1=" + hmac.new(bytes(settings.SECRET, 'utf-8'), bytes(event['body'], 'utf-8'), hashlib.sha1).hexdigest()
    if(signature != signedBody):
        return {"statusCode": 401, "body": "Unauthorized" }

    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    params = {"status": "テストツイートしてるぞー(" + datetime.now().strftime("%H:%M:%S") + ")"}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
    
    return {"statusCode": 200, "body": "つぶやけたぞー" }

