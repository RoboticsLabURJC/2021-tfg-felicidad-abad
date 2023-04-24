---
title: "Week 18. Trying to subscribe to one topic pt.2"

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
- week 18

author: Felicidad Abad
pinned: false
---


First approach. Trying to make a python script that returns the position of the robot to me.

This week I made my first attemp to make that script. The first step was to import the ListenerPose3d module from the pose3d script and initiate a node that could listen to it.

But i got a lot of errors. The first one and the one who worries me is that python can't seem to find the rospy module.
