---
title: "Week 48. Addind time.sleep to avoid errors & checking the exercise again"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- April
- selenium
- ROS
tags:
- GitHub
- week 48
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


Even after using the invisibility_of_element_located function, or the selenium methods to wait for an element to be clickable, some errors still happened.

It appears that the code is running faster than the changes in frontend, and because of that, some of the buttons Selenium need to click are not available when it tries to do it. The only solution I found to this problem, was to insert a time.sleep with one or two seconds.

The second task of this week was to continue checking the image processing exercise. The log file for the exercise.py, hal.py and gui.py was never created. So this time I tried a differente approach:

1. I executed the hal.py inside docker container directly, and printed the image variable. I could see that this variable has a correct value, so the problem apparently isn't here.
2. I executed the exercise.py directly inside docker container. There was no errors neither.
3. After trying them, I returned to the browser to launch my exercise. It kept doing nothing with the code inserted by the user. So I kept trying to debug, and by accident I realized that the prints forgotten inside the exercise.py show themselves on the console showed by the browser!! This is a really great discovery for me, as I could unlock some of the problems I have.
