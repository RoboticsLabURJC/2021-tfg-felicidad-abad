---
title: "Week 36. Implementing image processing exercise pt.2"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Unibotics
- December
tags:
- GitHub
- Unibotics
- week 36

author: Felicidad Abad
pinned: false
---


Afther checking everything was ok with raising the exercise, it was time to test it.

The problem appears here.

I wrote a pretty simple code upon the preloaded base (just creating a variable and using the HAL module functions to get the image and after that trying to show it in the visualization screen). After loading my code, the following error appeared

![](/2021-tfg-felicidad-abad/images/modules_error.png)

It seems that the modules HAL & GUI couldn't be initialized before using them, which I think is strange because the code in the exercise.py script already does that, so the user shouldn't have to do it.
