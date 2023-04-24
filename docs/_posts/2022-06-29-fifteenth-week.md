---
title: "Week 15. Understanding subprocess module"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- July
tags:
- selenium
- GitHub
- Unibotics
- week 15

author: Felicidad Abad
pinned: false
---

First thing I need to do in my functionality test: Make the RADI container available. In order to do that, normally, i would type ```docker start RADI``` in my linux console.

But now i need to do that inside a python script.

As I was talking with Jose Maria, he told me one of the previous students needed the same functionality for the unibotics tournaments and maybe I could try to use the subprocess library in Python.

As i didnt knew anything about that library, now i needed to make my own investigations in order to use it correctly.

This module give us the chance to work with process, similarly as I would do in a shell. I found two candidate functiones to do what i needed:

1. **subprocess.Popen()**
1. **subprocess.run()**

Both seemed to work well with that I wanted to do, si I picked the subprocess.Popen.

First step complete!
