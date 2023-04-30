---
title: "Week 47. Submit button obscured by a modal"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- March
- selenium
- ROS
tags:
- GitHub
- week 47
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


I found the reason for getting that timeout errors the previous week.

It was easy finding it, not so easy planning the resolution.

So, after inserting the user code into editor and clicking the "load into robot" button, a modal appears while it loads the code. If the time it takes for loading the code and making the modal disappears is higher than the time I put into time.sleep for the tests, the script returns an error because it cannot do the following step: click submit/play button.

Afther trying different ways, I found one that seems to work well, the method: invisibility_of_element_located. This method wait until the element selected disappears from the window and after that, it continue with the executing of the rest of the script.

How many time do we need to wait? To avoid getting stuck if the element, for some reason persists in the window, I put a timeout of 40 seconds. This may be enouth to load a user code but if not, it can be updated at any time with one simple change.

