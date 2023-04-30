---
title: "Week 39. Investigating how to handle topics"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- February
- selenium
- ROS
tags:
- GitHub
- week 39
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


The objective of these test is checking wether, executing the user code, the robot changes it position or not.

As the objective was clear, I started investigating some other ways of handling the messages of the topics in a simpler form.

I had the following points clear
+ The publisher was constantly publishing messages in the topic used by the selected exercise.
+ I only needed to check the messages two times
  + The first one, before executing the code
  + The second one, a few secons after executing the code
+ The comparison had to be different

With that in mind, I did not need all the messages published in the topic each exercise used. I needed the **correct** messages, the ones that allowed me to compare and check if the exercise is working or not.

After a lot of investigation, I finally found the command `rostopic echo`. This allowed me to check the messages a publisher is sending and, as I only need one I tested how to ask with rostopic echo for just one of these messages.
