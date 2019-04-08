#coding: UTF-8
import json,hashlib,hmac
from requests_oauthlib import OAuth1Session
from datetime import datetime
import settings

def lambda_handler(event, context):
    # HMAC値による簡易認証処理
    signature = event['headers']['X-Hub-Signature']
    signedBody = "sha1=" + hmac.new(bytes(settings.SECRET, 'utf-8'), bytes(event['body'], 'utf-8'), hashlib.sha1).hexdigest()
    if(signature != signedBody):
        return {"statusCode": 401, "body": "Unauthorized" }
    
    # プルリクの情報を抽出
    body = json.loads(event['body'])
    
    # actionのキーがなければ終了
    if "action" not in body:
        return {"statusCode": 200, "body": "exit" }
    
    # プルリクのクローズでなければ終了
    if body['action'] != "closed":
        return {"statusCode": 200, "body": "exit2" }
    
    # ツイートで必要な情報を取得
    title = body['pull_request']['title'] # プルリクのタイトル
    html_url = body['pull_request']['html_url'] # プルリクのURL
    user = body['pull_request']['user']['login'] # プルリク作成者
    merged_by = body['pull_request']['merged_by']['login'] # マージ者
    
    # GitHubのアカウントとツイートする際の名前の対応表
    user_list = {
        "nsuzuki7713": "なおと",
        "TsutomuNakamura": "tsutomu",
        "tokidrill": "Toki",
        "minokich": "みのきち",
    }
    
    # tweet文章作成
    msg = user_list[merged_by] + "さんが"\
        + user_list[user] + "さんのプルリクをマージしました😊" + "\n"\
        + "【" + title + "】となります😎️" + "\n" +html_url

    # tweet処理
    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    params = {"status": msg }
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
    
    return {"statusCode": 200, "body": msg}

