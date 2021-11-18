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
description: "記錄當天的課題與解決，新發現，與新改善點"
socialImage: "media/image-2.jpg"
---

# 本期重點

 
# 第二步：明确与读者的联系（Why）

## 1.勾勒典型场景 用一个大家经常遇到的情景来引入。
## 2.塑造典型冲突 场景背后会有一个冲突，可能是未达预期，可能是遭受失败。
## 3.提出核心疑问 为什么会产生这种冲突？我们应该如何解决？

# 第一步：明确主题（What）

# 第三步：找到关键答案（How）

## 1.推理法。层层推进，找到问题的根源。

## 2.归纳法。把一系列答案，归总于几个大类，然后分类表述。

## 3.步骤法。给出具体的操作步骤。
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
    