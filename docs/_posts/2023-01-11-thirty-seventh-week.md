---
title: "Week 37. Modules problem & returning to automatic testing for a while"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Unibotics
- December
- selenium
tags:
- GitHub
- Unibotics
- week 37
- Selenium

author: Felicidad Abad
pinned: false
---


So, it looks like there is some problem with the PYTHONPATH in my new exercise, and because of that the modules cannot be "seen" when the code from user is executed. As I find a little hard to debug these topics, I decided to return for a little bit to the automatic testing part.

This week I discovered another way of working with the WebElements in Selenium. The class Actions Chains. As I kept investigating I learned that this class is the one should be used when simulating complex actions like, for examplen drag and drop or pressing some keyboard letters.

Although Actions Chains was useful and not returned an error, the tests kept failing because they were not inserting code in the ace editor either.
