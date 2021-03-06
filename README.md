# Emerging-Technologies-Project-2017

This is my repository for my Emerging Technologies Project which reads a users input on canvas and predicts the number the user has drawn using the MNIST neural network. 

Using Javascript, html and python I created a web app that allows a user to draw a number on a canvas for tensorflow and keras to predict the number that was input.

Unfortunately with a few complications I wasnt able to get the predictions.

## Requirements
* Python
* Keras
* Tensorflow
* Flask

## How to run
When you have the project downloaded onto your local machine just use your command prompt in order to start it up.

You need to direct to the projects folder and use "python script.py" in order to start up the server and flask.

Once that's done just use 127.0.0.1:5000 in your browser to start it up.

## Project instructions.

### Project 2017

The following are your instructions to complete the project for the module Emerging Technologies for 2017. This project is worth 40% of your marks for the module. Please see the course homepage for the deadline.

### Overview

In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

### Instructions

Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
Add a route to your application that accepts requests containing a user input image and responds with the digit.
Connect the HTML page to the route using AJAX.
Submission

To submit your project, you must make your git repository available using a git hosting service like GitHub or GitLab. Use the submission link on the course webpage to submit the URL for your hosted repository. You can submit at any time before the deadline, the earlier the better, as the last commit you make to the repository before the deadline will be corrected irrespective of when you submitted your link. If your repository is private you must add the lecturer as a collaborator.

