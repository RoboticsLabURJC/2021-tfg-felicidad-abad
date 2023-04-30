---
title: "Week 43. Insert code in ACE editor resolved"

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
- week 43
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


Finally this week the problem of inserting code in the ACE editor is resolved!

The problem was in the class **LiveServerTestCase** and how it treats the statics files. It seems that this class has some problems managing this kind of files. That's why the static files (like css, etc) were no loading correctly.

This made us unable to insert code into the editor, because it didn't loaded right.

Changing the **LiveServerTestCase** for the **StaticLiveServerTestCase** class, solved it. This second class has no problem loading the static files.

There is not a lof of information about this online. I had to do research in a google forum conversation and the documentation page por Selenium, but after that, the information available was strill scarce.

I'll keep trying to completely understand this problem in the following weeks, as it was a stopping point for a long part of my TFG.
