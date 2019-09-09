
# Django Workshop

## Workshop Outline:

### <a href="https://github.com/micleners/django-workshop/tree/level-1-no-custom-auth">Level 1: API and Template Basics</a>
Level 1 is recommended for all to start with. If you'd like, you can continue on to Level 2 without implementing Custom auth after finishing level 1.
1. Project Startup (prerequisite)
2. ~~Create Custom Auth Model (optional)~~
3. Create Event Model
4. Explore Django Admin
5. Event Serializer, View and URLs
6. Django Template and View for List View

### <a href="https://github.com/micleners/django-workshop/tree/level-2-custom-auth-and-deploy">Level 2:  Custom Auth, Advanced Views, Templates and Heroku Deploy</a>
Level 2 starts the same as Level 1 with the added best practice foundation of a custom auth model. However, you should be able to advance from Level 1, Part 6 to Level 2, Part 7 without the custom auth model.
1. Project Startup (prerequisite)
2. Create Custom Auth Model (optional)
3. Create Event Model
4. Explore Django Admin
5. Event Serializer, View and URLs
6. Django Template and View for List View
7. Command Line Inspection of Model Objects vs Serialized Object
8. Deploy to Heroku
9. Django Template and View for Create and Delete with Crispy Forms
10. Repeat Model, Serializer, View and URLs flow with Locations

# Prerequisites

- Have Python3 installed on your system
- Create a virtual environment with Django and Django Rest Framework installed
- Have a text editor (I recommend [VS Code](https://code.visualstudio.com/) if you are in the market)

If you need help getting set up, I recommend you check out [this useful book chapter](https://djangoforbeginners.com/initial-setup/). If you have a different virtual environment you like to use, feel free to install django and DRF however you prefer.

# Clone and Checkout Branches

Level 1 and Level 2 have been completed on two different branches on git. To get the source code for this workshop, you can clone this repo: `git clone https://github.com/micleners/django-workshop.git`

You can begin by working off of `master`, which sets up the project as found in the `Prerequisites` and `Section 1` below. You will still need to make sure to setup your virtual environment correctly.

Then, checkout the appropriate branch for the level you are working on:
- `git checkout level-1-no-custom-auth`
- `git checkout level-2-custom-auth-and-deploy`

You can reset the head back to a certain commit to help you figure out how to get unstuck if needed. Alternatively, you can check out the code on github where the tutorials are located:
- <a href="https://github.com/micleners/django-workshop/tree/level-1-no-custom-auth">Level 1: Novice - Less Production Ready</a>
- <a href="https://github.com/micleners/django-workshop/tree/level-2-custom-auth-and-deploy">Level 2: Advanced - Custom Auth and Heroku Deploy</a>