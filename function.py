#coding: UTF-8
from modules.requests_oauthlib import OAuth1Session
# import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

params = {"status": "ローカルのpythonからつぶやいているぞー。呟けている？？ #shinjukumokumoku"}
# params = {"status": "AWSのLambdaからつぶやいているぞー。呟けている？？ #shinjukumokumoku"}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)

print('つぶやけたぞー')