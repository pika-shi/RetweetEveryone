#!/usr/bin/env python
#-*- coding: utf-8 -*-

import twitter
import sqlite3
import time

con = sqlite3.connect('Tweet.db')

CONSUMER_KEY="**********"
CONSUMER_SECRET="**********"
ACCESS_TOKEN="**********"
ACCESS_TOKEN_SECRET="**********"

api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET,
                      cache=None)

since_id = 0
while 1:
  time.sleep(60)
  try: TL = api.GetFriendsTimeline(since_id=since_id)
  except: continue
  if not TL: continue
  since_id = TL[0].id
  for tweet in TL:
    try:
      if tweet.text[:4] == 'RT @':
        colon = tweet.text.find(':')
        user = tweet.text[4:colon]
        text = tweet.text[colon+2:]
        u = api.GetUser(user)
        con.execute('''insert into tweet values ('%s', '%s', %d, '%s', '%s', %d, '%s')'''
                    % (u.name, user, tweet.id, text, tweet.user.screen_name,
                       tweet.created_at_in_seconds, u.profile_image_url))
        con.commit()
    except:
      continue
