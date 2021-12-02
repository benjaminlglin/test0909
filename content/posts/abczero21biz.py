import io
import os
import sys
import datetime
tp1='''---
title: {0}東X米筆記
date: "{0}T23:46:37.121Z"
template: "post"
draft: false
slug: "{1}"
category: "每日學習記錄"
tags:
  - "工作記錄"
  - "生活管理"
description: "在事上磨練。記錄當天的課題與解決，新發現，與新改善點,1.01的365次方"
socialImage: "media/image-2.jpg"
---

# 每天陪小孩做作業一人15分鐘
> 這是一種投資

 
# 每天進步事項


# 小目標
- 主日禱告操練

# 語言學習鍛煉


'''
os.chdir('C:\\Users\\youth\\Documents\\gitdocs\\test0909\\content\\posts')
dt_now = datetime.datetime.now()
fn=dt_now.strftime('%Y%m%d%H')
fn2=dt_now.strftime('%Y/%m/%d')
fn3=dt_now.strftime('%Y-%m-%d')
os.mkdir(fn)
print(fn)
print(dt_now)
args=sys.argv
slug="pleaseDecribe"
if (len(args)==2):
    slug=args[1]
    print(slug)

with open("./{}/init.md".format(fn), mode='w',encoding='utf8') as f:
    f.write(tp1.format(fn3,slug))    
    