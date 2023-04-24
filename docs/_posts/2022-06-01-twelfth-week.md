---
title: "Week 12. Uploading frontend automatic testing"

sidebar:
  nav: "docs"

#toc: true
#toc_label: "TOC installation"
#toc_icon: "cog"
classes: wide

categories:
- Selenium
- May
- June
tags:
- selenium
- GitHub
- Unibotics
- week 12

author: Felicidad Abad
pinned: false
---

Once the test are made, it was time to make one file that contained them all.

When deploying to production, no matter how small the changes are, it is necessary to check that everything continues to work. Thats why we joined them in only one script, so when the changes are uploaded to production all of the previous thing in production are tested.

Once the test are over, we should see a message like the following one

![](/2021-tfg-felicidad-abad/images/captura-test-resultado1.png)

In the console, we will be able to see how many test were executed, how much time was spend on it and of course the results of them. In this case, all test went well but if some of them failed we'll see how many of them and in which lines of the tests were the errors located.
