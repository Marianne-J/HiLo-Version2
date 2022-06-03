# Overview

This is a game of HiLo, based on a version of the game I helped write previously and improved on from a version I recently wrote in Java. The object of the game is for the player to guess whether a randomly generated number between 1 and 100 will be higher or lower than the current number displayed. If the player guesses correctly, they will recieve points. If the player guesses incorrectly, they will lose a life. The game ends either when the player chooses to quit or when the player runs out of lives.

My purpose in writing this program was to learn how to work with a cloud database and integrate it into a program.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video]()

# Cloud Database

I used the Firestore database that comes with a Google Firebase project. The structure is simple and contains one table, which holds the users. Each user has a username and high_score attribute that holds a user's name and high_score respectively.

# Development Environment

* Firebase
* Visual Studio Code
* Python 3.9
* Git / GitHub

# Useful Websites

* [Firebase Documentation](https://firebase.google.com/docs/firestore)
* [Google Cloud Documentation](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)

# Future Work

* Improve data security
* Switch user name to user ID for document name