---
title: "Week 44. Implementing individual functionality test"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- March
- selenium
- ROS
tags:
- GitHub
- week 44
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


After the issue with ACE editor was solved in the previos week, my main task this week was to start implementing the test exercise by exercise.

The first one I choosed for this task is the follow line exercise. As I already knew the topic this exercise uses, preparing the test for it required to put together the job I had done in the previos weeks.

But as I developed this test, I found some things to keep in mind.

First, I have to make sure the RADI container is up before I try to do test the exercises. Otherwise, they wont be able to launch the exercise neither executing the user code afterwards.

Second, everything that the test needs to do takes time: launching the exercise, loadind the user code into the robot, etc. To be able to do this, I need to be able to wait until every actions is completed, otherwise Selenium will return an error as it won't be capable of clicking the necessary button or performing another actions. This is really important, but while I search for ways to control it into code I'll put time.sleep between actions.

