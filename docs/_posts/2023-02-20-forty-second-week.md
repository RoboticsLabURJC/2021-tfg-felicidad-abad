---
title: "Week 42. Trying to debug image processing exercise"

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
- week 42
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


While the error when inserting code in ACE editor seems close to be resolved, this week I returned to the exercise implementation.

There was a problem with the PYTHONPATH value, as explained the previous weeks. I don't relly know why it wasn't able to locate de modules hal & gui, because there were no problems with the rest of the exercises.

But one that is configured, the error shown in previous blog entries dissapeared.

Still, the image I was trying to show did not appear in the visualization window. Apparently there is no error with the modules neither with the user code, which passes the pylint checker without a problem.

I'll keep trying to resolve this issue.
