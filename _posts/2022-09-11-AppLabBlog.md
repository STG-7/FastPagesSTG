---
toc: true
layout: post
description: AppLab HACKS
categories: [Week 3]
title: AppLab HACKS
comments: true
--- 

### AppLab Planning/Blogging 

Planning:
- 3 Question quiz on Python syntax
- Final score and percentage is outputted at the end
- Design should look neat and well connected

Blogging:
At first I used the code tab to implement buttons and position of the bottom and then use on-event code for each of those buttons. After the first set of questions I realized that this is not efficient and started using the design tab to place buttons and other features on the screens. From there I used the code tab and coded in javascript to use these buttons and labels. 



### AppLab Creation

[Quiz-AppLab](https://studio.code.org/projects/applab/yrwPro-CrNcHUNN8dMl2ptFtyLiGMMKfnJsrWg_sqjs)

Extra features in the program:
- Explanations for right and wrong answers for every question in the quiz
- Final Percentage and accuracy of each question is posted at the end
- Use of "if" conditional statements and JavaScript code to further enhance the App


### Relating AppLab to College Board Performance Task



#### Purpose: 

The purpose of this program is to test the user’s understanding in Python syntax.


####  Functionality:  

This program consists of 15 different screens and tests users on 3 different questions relating to Python. It starts with a home screen that allows users to click a button that takes them to the first question and different answer options. Each of those options when clicked on will take the user  to a seperate screen that tells whether the answer is correct/incorrect and gives an explanation. On the bottom of these screens are a button that can take you to next question. After the final question is answered there will also be a button on the bottom of the "explanation" screens that will take you to the final page. This page outputs which questions you got correct and the final percenage.



#### Data Abstraction:

Each of the answer buttons in the questions page had their own functionality abstracted in one method. The explanations for right/wrong, the button to move on to the next page, and the backend process of calculating correct/incorrect was all done in one method for each question. To further improve this code I can further abstract the data by adding a list of dictionaries that contain key-value pairs for questions and answers.



#### Managing Complexity:

In order to manage the complexity of this quiz, I was able to type many comments and ordered my code in a readable fashion in order to ensure that the code is very easy to follow. The comments allow us to communicate what we are doing with each function and what the purpose of the variables are. And the repeated use of the functions allow us to easily call back to a known function that we make and it communicated the purpose of the funciton without having the reader have to understand the code.

#### Procedural Abstraction:

The first function allows the user to start the quiz, after that there is a series of functions that display a question and answer buttons that have different outcomes for every different answer button. At every new page that was called from the answer button there is a function that allows the user to go to the next question and then finally the last qusetion. All along backend processes and calculations occur calculating which question the user got correct and the final percentage that is displayed in the last page/



#### Algorithm Implementation:

I used similar algorithms for every answer button in the questions pages but each screen change for question and the final page had different algoritmn implementation. To further improve this code, we can reduce repition for the answer buttons algorithms.




#### Testing: 

I tested this quiz multiple times, both in the process of creating the quiz and even after I fully programmed it. I tested every screen's output and tested the validity of the final percentage in the last screen.

