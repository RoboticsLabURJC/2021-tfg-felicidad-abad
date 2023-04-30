---
title: "Week 50. User code gets emptied at parsing"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- April
- selenium
- OpenCV
- Unibotics
tags:
- GitHub
- week 50
- Selenium
- OpenCV
- Unibotics

author: Felicidad Abad
pinned: false
---


I located the problem: **the code from the user was being deleted inside the exercise.py** so, what I need to do now is finding the point where it gets emptied.

There are two variables that contains part of the code:
1. iterative_code
2. sequential_code

I debugged the function seperate_seq_iter, where both of them were created. This function was returning two empty strings, so maybe the problem was here?

No. That would've been easy, but the code this function received was already empty. So... I ned to keep debugging.

As I kept debugging, I found a try catch inside the parse_code function. It tries to get the debug level and then the rest of the code. This part seems to be old code, so the flow went to the catch and in this catch the code from the user changed to an empty string.

Here was the problem!

I commented that part of the code, stablished the debug level to 1 and after that called the seperate_seq_iter function to get the iterative and sequential code.

After this, the exercise already worked! :) I'll add a gif that shows the exercise working. I still need to record my own video:

![](/2021-tfg-felicidad-abad/images/image-processing.gif)
