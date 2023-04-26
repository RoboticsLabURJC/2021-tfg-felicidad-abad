---
title: "Week 35. Implementing image processing exercise"

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
- week 35

author: Felicidad Abad
pinned: false
---


Once the manager.py and the flow is understood, it was time to really start implementing the exercise.

As a base, I used the color_filter exercise. The goal of this exercise is to understand the space of color and make filters upon the image the webcam captured.

To implement the exercise the first task was adding some little things to the manager. Otherwise it wouldn't know which exercise needs to serve when called with image_processing id or which things are needed for it.

Also, I had to update the instructions.json file. The change was really simple, as this exercise is not gonna use a robot.
