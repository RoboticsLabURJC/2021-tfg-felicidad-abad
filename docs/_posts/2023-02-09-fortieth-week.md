---
title: "Week 40. Simplyfying and reusing scripts"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- December
- selenium
- ROS
tags:
- GitHub
- week 40
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


With the fidings of the previous weeks, maybe two or three scripts per exercise were not really needed.

Following this idea, I created a shell script for one of the topics that a lot of exercises use. In this case, the F1ROS/odom. This topic pass the coordinates of the robot so it was exactly the message we need to do the test. Besides, there are a lot of exercises that uses this, so I think this is a great point to start.

As I couldn't insert text in the ACE Editor yet, the approach was to make a simple code for one of the exercises in a D1 deployment and, after that, calling two times the shell script to check from outside the contaier to check it the position is really changing and this approach is the correct.

It worked really well!

Now, I just needed to check the format that this shell script will return if used in a subprocess.
