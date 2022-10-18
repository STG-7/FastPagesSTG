---
toc: true
layout: post
description: Week 9
categories: [Week 9]
title: Script for First Check Video
comments: true
--- 


### Program Purpose 

- An online single-player minesweeper game that can be played anywhere, anytime
- Users could choose to store data such as high scores (minimum number of moves or time) if they wish.

### Program Function

- Function is similar to that of a minesweeper game [Minesweeper](https://www.google.com/search?q=minesweeper+game&rlz=1C1CHBD_enUS930US930&oq=minesweeper+game&aqs=chrome..69i57.1801j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on)

Order:
1. User will click on a coordinate in the "game grid"
2. If the coordinate is a "safe square", then it and the surrounding "safe squares" will also be "flagged":
3. If the coordinate is a mine, then the game ends, revealing all of the mines 
4. Top score will be saved using python lists
