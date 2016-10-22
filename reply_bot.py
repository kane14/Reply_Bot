#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
from datetime import timedelta
import datetime

CK="XXXXXXXXXXXXXXXXXXXXXXXX"
CS="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AT="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
AS="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)#世界標準時から日本時間に

	# リプライが来たら返信
        print(status.text)
	print(str(status.in_reply_to_screen_name))
	print(str(status.user.screen_name))
	if str(status.in_reply_to_screen_name)=="{Bot_TWITTER_ID}" and str(status.user.screen_name)=="{Twitter_ID}":
		tweet = "@" + str(status.user.screen_name) + " " + "Yeah!\n" \
			+ str(datetime.datetime.today())
		api.update_status(status=tweet)
	return True
     
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
     
    def on_timeout(self):
        print('Timeout...')
        return True
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
