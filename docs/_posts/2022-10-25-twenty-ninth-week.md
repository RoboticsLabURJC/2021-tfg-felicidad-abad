---
title: "Week 29. Trying to insert code in ACE editor pt.3"

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
- week 29

author: Felicidad Abad
pinned: false
---


As I already knew the edits is a WebElement, I looked for ways of interacting with it using Selenium and asked my co-tutor about it. It seems that there is another way of sendint text to them, the function execute_script.

This function is used when the functions provided by Selenium can't interact with an element. This functions executes Javascript code. This function is also used in a platform similar to Unibotics so it looked good.

Unfortunately... it didn't work either.

![](/2021-tfg-felicidad-abad/images/ace-insert-error3.png)

This time was a different error, at least.

