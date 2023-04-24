---
title: "Week 24. Adding a .sh script to be able to execute topics_testing.py"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- September
tags:
- selenium
- GitHub
- Unibotics
- week 24

author: Felicidad Abad
pinned: false
---


As i was trying to test the .sh script made the previous week... i got another error.

It seems that the configuration I added a lot time ago to the bashrc to use the rospy library was missing when I executed the script from outside the container...

The only solution seems to be adding a new line to the script which executes the line added to bashrc before trying to execute the script.
