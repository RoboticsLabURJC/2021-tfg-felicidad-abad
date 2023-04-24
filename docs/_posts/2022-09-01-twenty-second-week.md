---
title: "Week 22. Trying to get the position from outside docker container"

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
- week 22

author: Felicidad Abad
pinned: false
---


Once I had the script already working inside the container it was time to test it outside of it, in the same script as the test were being made.

In first instance as i didnt want to contamine that script, I made another really simple one. This script just executed the following command as an subprocess and printed the output: docker exec -it RADI /RoboticsAcademy/exercises/follow_line/web-template python3 topics_testing.py

Unfortunately it returned an error telling me that I had no permission to do that. I tried to gave the necessary permissions but it was unsucessful.

I'll come back with another idea.
