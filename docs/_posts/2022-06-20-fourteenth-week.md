---
title: "Week 14. Functionality test draft"

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
- week 14

author: Felicidad Abad
pinned: false
---

Once the frontend tests are finished and working, the next step is to start with the functionality tests for the production exercises.

This week we evaluated a first idea. This is how ideally we want the test to work, but a lot of work and investigacion is yet need to be done.

The idea is as follows:
1. We have a file that runs. This file must:
    1. Raise the RADI container
    1. Test that I can connect to it.
    1. Test that I can raise the exercise
    1. Insert code in the ACE editor
    1. Check after a while that the position of the robot has changed.
    
Let's start with the basic: trying to raise the docker container from a script.
