---
title: "Week 16. Checking ROS topics"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- July
tags:
- selenium
- GitHub
- Unibotics
- week 16

author: Felicidad Abad
pinned: false
---


I already could raise the RADI container and I knew how to use Selenium to raise a test server. So a few steps of the integration were already done.

There were a few more things I needed to know. For example, ROS topics, the ones who were going to give me the robot position.

The problem is, I initially have no idea what a "topic" is. So this week my main task was getting to know a little about ros.

I learned quite a few things about these topics, for example:

1. They are unidirectional, and one or various nodes can publish messages in them. (publishers)
1. Other nodes may subscribe to them. (subscribers)
1. Each topic has a message format asociated
1. Topics have to be unique

This seems interesting, hope I can make some progress soon.
