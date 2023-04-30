---
title: "Week 46. Changing the selection to react & test getting timeout"

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
- week 46
- Selenium
- ROS

author: Felicidad Abad
pinned: false
---


The main menu, where the exercises are collected, changed to react a while ago. So now that I have a basic functionality test working, it's time to change the way I'm selecting the exercise, so it works too with the new frontend of exercises menu.

```sh
element = self.selenium.find_element(By.XPATH, f"//div[@card-id='{self.exercise.exercise_id}'")
```

Also, while executing the test I noticed that, depending of how much time launching or loading the code into the robot takes the test may fail.

Before changing the subprocess.Popen for subprocess.run it also failed because the publisher was not publishing any messages into the topic, and the test got stuck trying to get some message.

Now, it got stuck after loading the code into the robot. I'll check why and come with a solution next week hopefully.

