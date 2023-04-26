---
title: "Week 26. Subprocess invoking .sh indifinitely waiting"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- September
- October
tags:
- selenium
- GitHub
- Unibotics
- week 26

author: Felicidad Abad
pinned: false
---


As I added the subprocess line to the Selenium script I noticed that it got stuck and never gived an answer unless I stopped it manually.

I tried to replicate that error directly inside the container, and I discovered that, if roscore wasn't launched then the script did not returned anything at all. For the moment, I put another line inside the .sh script to execute roscore but... I wonder if it is really necessary. In the moment the pseudo user launches the exercise roscore should be operative I think? Maybe this error is because my Selenium script is not complete yet.
 
![](/2021-tfg-felicidad-abad/images/sh-script2.png)
