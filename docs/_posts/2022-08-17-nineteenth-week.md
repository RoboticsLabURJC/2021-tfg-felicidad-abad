---
title: "Week 19/20. Trying to subscribe to one topic pt.3"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- August
tags:
- selenium
- GitHub
- Unibotics
- week 19
- week 20

author: Felicidad Abad
pinned: false
---


The problem with rospy continues, i can't seem to find from where it comes so I need to ask for help to the rest of developers of unibotics.

Thankfully, they seem to find where it is. It's a configuration problem!

I keep getting the following error because somehow I didnt have the environment variables needed to use ROS noetic even tho the exercises worked.
![](/2021-tfg-felicidad-abad/images/rospy-error.png)

Once I added this line to the .bashrc and restarted the container, that error disappeared: ```source /opt/ros/noetic/setup.bash```
