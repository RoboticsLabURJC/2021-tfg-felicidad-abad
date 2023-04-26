---
title: "Week 27. Trying to insert code in ACE editor pt.1"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- October
tags:
- selenium
- GitHub
- Unibotics
- week 27

author: Felicidad Abad
pinned: false
---


Once I have the topic part, the next step is interacting with the ACE editor that the platform uses.

As I already had a test to make loging that inserted text into an area, my first instict was to use the same function this time. I searched through the .html of one of the exercises to find the id of the editor, so I interact with it through Selenium. However, it seems that I can't do that with the ace editor as it returns the following error

![](/2021-tfg-felicidad-abad/images/ace-insert-error.png)

