---
title: "Week 49. Code sent by the user is empty"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- April
- OpenCV
- Unibotics
tags:
- GitHub
- week 49
- OpenCV
- Unibotics

author: Felicidad Abad
pinned: false
---


So, with the discovery of the previos week, I now can debug with more ease.

My first instinct was that maybe, even after configuring the PYTHONPATH, the modules were not importing correctly and because of that I tried to find the problem there. But this time, that part of the code was working correctly.

I tried after to check where the code from the user was getting executed and to see what it returned as I took the base for the color_filter exercise. The return of that execution was empty, but it was normal the code used an exec function.

The next natural step was to check the code the exercise.py was trying to execute. Empty. So... the problem seems to be here. Maybe the exercise.py is not receiving the code correctly? Or maybe the problem comes from other part?
