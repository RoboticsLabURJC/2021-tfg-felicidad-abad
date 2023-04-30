---
title: "Week 45. Differences between subprocess.Popen & subprocess.run"

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
- week 45
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


As I commented the previous week, one thing I need to keep in mind for these integration is that the RADI container must be up before trying to execute the necessary test.

For that reason, I started investigation different subprocess modules. The two modules that adjusted more to what we need are the following ones: subprocess.Popen and subprocess.run.

There is more things different between them that the one I'm gonna write, but this one in particular is the one that made me choose subprocess.run for the Selenium test.

1. **subprocess.run**: Waits till the subprocess finishes and then continues executing the principal program.
1. **subprocess.Popen**: Does not wait for the subprocess to finish before continuing executing the principal program.

Because of that, I decided to change the module used in the tests. It may take a few seconds more, but it prevents errors caused by the RADI container being off.

