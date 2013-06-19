#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sqlite3
import time

con = sqlite3.connect('Tweet.db')
TL = con.execute('''select * from tweet order by time desc limit 300''').fetchall()

html = '''Content-type: text/html; charset: utf-8

<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset= "UTF-8">
    <title>みんなのリツイート</title>
      <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/bootstrap-responsive.min.css" rel="stylesheet">
          <script src="js/jquery.js"></script>
            <script src="js/bootstrap.min.js"></script>
            </head>
            <body style = "padding-top:30px;padding-bottom:20px">
            <div class ="container">'''

for tweet in TL:
    tm = time.localtime(tweet[5])
    tm = '%d/%d %d:%d' % (tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min)
    html += '''<div class="row-fluid">
    <div class="span3"></div>
    <div class="span6">
      <div class="well">
        <div class="row-fluid">
          <div class="span2">
            <div align="center">
              <img src="%s">
            </div>
          </div>
          <div class="span8">
            <b><font size="3">%s</font></b>
            <font color="#999999">%s</font><br>
            <div style="padding-top:10px;"></div>
            <font size="3">%s</font><br>
            <div style="padding-top:5px;"></div>
            <font color="#999999">@%s がリツイート</font>
          </div>
          <div class="span2">
            <font size="3">
              <a href="https://twitter.com/%s/status/%d">%s</a>
            </font>
          </div>
        </div>
     </div>
   </div>
   <div class="span3"></div>
 </div>''' % (tweet[6].encode('utf-8'), tweet[0].encode('utf-8'),
             tweet[1].encode('utf-8'), tweet[3].encode('utf-8'),
             tweet[4].encode('utf-8'), tweet[4].encode('utf-8'),
             tweet[2], tm.encode('utf-8'))

html += '''</div>
</body>
</html>'''

print html
