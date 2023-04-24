---
title: "Week 13. Explaining the test, note to my future self"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- June
tags:
- selenium
- GitHub
- Unibotics
- week 13

author: Felicidad Abad
pinned: false
---

Although the test code may seem simple or repetitive at first glance, there is a lot behind it. That's why I think it's good to make this blog post, even if it's just to remind myself how it all works in the future.

The first thing we need to know is that the setup function raises a django server where to do the tests. Thanks to this server we can run the tests.

There are also two related files: **operations.py and test_frontend.py** 

### operations.py 
This file is really important. Because the Selenium server is going to create a default database that will be empty, so we need to create the exercises and test users in each test.

### test_frontend.py 
This is where the tests are located. Between the imports, we reference the previously explained file to be able to use the functions.

Within test_frontend each exercise is a class, which allows us to launch them individually if necessary either to test the changes before committing or via GitHub actions.
