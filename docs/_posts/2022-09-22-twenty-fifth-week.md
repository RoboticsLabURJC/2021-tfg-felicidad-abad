---
title: "Week 25. Invoking testing.py through a .sh script"

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
- week 25

author: Felicidad Abad
pinned: false
---


I already made the .sh script. 

![](/2021-tfg-felicidad-abad/images/sh-script.png)

When I execute it, it returns a lot of things, including the posicion of the robot as showed in the following image:

![](/2021-tfg-felicidad-abad/images/sh-response.png)

For now, the flow of the test is quite complicated. In first place, the selenium script uses a subprocess to call the .sh script inside the container. This .sh script sets the confiuration and then calls the testing.py script which recovers the position of the robot.
