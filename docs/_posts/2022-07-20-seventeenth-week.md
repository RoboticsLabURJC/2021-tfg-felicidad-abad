---
title: "Week 17. Trying to subscribe to one topic"

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
- week 17

author: Felicidad Abad
pinned: false
---


I already had a little notion of what a ros topic is, so now it's time to start coding and finishing to understand how they really work.

I needed to do it for a lot of exercises, but i choosed to start with the obstacle_avoidance as it seemed quite normal.

The first thing was making sure I could find the topic that exercise was using, so i read the code of it. 

I could find that the position was set in the pose3d file, but not the topic it was using.

Luckily, there were some old files in the repository in which i could find the topic used!
![](/2021-tfg-felicidad-abad/images/obstacle-avoidance-topic.png)

I'll try to make a little python script that allows me to subscribe to that topic and check the position.
