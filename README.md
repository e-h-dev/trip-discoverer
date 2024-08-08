# Third Milestone Project

![Trip Doscoverer Logo](/static/images/icon.png)

# Trip Discoverer

![Trip Discoverer Theme Image](/static/images/hero-image.jpg)

## Table of Contents

- [Third Milestone Project](#third-milestone-project)
- [Trip Discoverer](#trip-discoverer)
- [Table of Contents](#table-of-contents)
- [Project Rationale](#project-retionale)
- [About](#about)
- [User Experiance (UX)](#user-experience-ux)
  - [User stories](#user-stories)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Flowcharts](#flowcharts)
- [Bugs](#bugs)
# About

Trip Discoverer, is an easy to use website, designed for anyone to access. The website provides up to date and 
clear information, for anyone looking for a nice day out. The options range from family to adult to kid friendly places. Users can also sign in and add their own Trips for the benefit of others.

## User Experience (UX)

### User Stories

#### Website Owner Goals

- We want the website to attract a new and wide range of users.
- We want an attractive website, where the information is clear, and easy to access.
- We want the users to have the ability of signing in, to add their own trip ideas.
- We want to be able to collect data from all users, to find their preferential category of trips, and places they visit.
- We want to be able to provide consumer habit information, to small local businesses, to promote their business to our users.
- We want the website to be responsive to all devices.

#### Site Visitor Goals

- I want to have access to clear details regarding all the trips detailed by the website.
- I want to be able to easily search for my preferred trip, by location and category.
- I want to add my own trip ideas to the website's database.
- I want to be able to edit my trip ideas on the website's database.
- I want the site to be responsive to my device.
- I want the site to be easy to navigate.

## Wireframes

Wireframes were created for mobile, tablet and desktop using balsamiq.

### Home Page

![Home Page](assets/wireframes/wireframe-home.png)

* The next wireframes cover the same layout. The Register page and Login page share layout, and the New Trip and Edit trip pages share layout. I have therefore, provided one wireframe for each group.

### Register / Login Page

![Register / login Page](assets/wireframes/wireframe-login.png)

### New / Edit Trip Page

![New / Edit Trip Page](assets/wireframes/wireframe-new-trip.png)

## Flowcharts

- The flowcharts below, show how the app is designed, to allow users easy navigaiton across all sections, and functions of the app. I ahve also colur coded the for functions CRUD (create, read, update and delete), each of the funtions are colured in the flowchart showoing how the app follows these four criteria.

### Admin flowchart

![Admin flowchart](/assets/flowcharts/admin-flowchart.jpg)

### User flowchart

![User flowchart](/assets/flowcharts/user-flowchart.jpg)

# Bugs

## Solved Bugs

| Number | Bug | Failed Atempt to fix | How I fixed the bug |
| :--- | :--- | :--- | :--- |
| 1 | When updating font-size in the navbar the size would not upate from the generic materialize font. | N/A | Looking in devtools, I saw fontsize in style.css was not working, since the original fontsize was on the materalize css as 15px. I updated the class 'fonts' on each of the nav list items rendering the larger font. |
| 2 | The register form was not running, the app rendered a flask error. | N/A | I had put the wrong name attribute for the password input. |
| 3 | To create a delete confirmation message, I tried to create a button which activates a javascript funtion creating a new button to the Dom with href link to the python delete function. This did not work. | I realised that the python route which the delete funtion activates is a backend function connectiing the app to the mongo data base, the javascript function will only speak to the DOM as a front end html builder rendering the url_for to the python function useless. To fix this issue I checkeded the href in devtools and an id number was rendered by the python funciton via the ulr_for. I copied this id based link ans updated the href which javascript was creating for the DOM, this fixed the bug, an the delete button created by javascript deleted the trip. The bug fix failed however, because it only wirked for the trip with that id, no other trip could be deeted. | To fix this bug I wrote the html for the confirmaton and hid it with display none in css. The javascript funciton changes the display prperties of both buttins hiding the first delete button and reveaing the confirmation button. This fixed the main problem but I created another bug. (see bug 4) |
| 4 | This above fix was not good enough as this caused a second bug. The javascript function only worked on the first trip of the list, for the rest of the items on display the delete button was inactive. | N/A | The reason for this bug was, I targeted the HTML elements with javascript via the ids. In javascript only one identical id could be used. I changed the funciton to target the HTML class created a for loop to iteraete over all instanses of the class, this way the delete confirmation was active on all trips dispalyed. |
| 5 | When logging into admin account, the page layout was distorted and most of the trip displays would not open. | N/A | After studying the code I realised the classes to connect the javascript were not in the correct palce in the admin section of the jinja if statement. By reseting the classes in html the page loades correctly. |
| 6 | Date stamp format was not clear looking like this Added on: [7, 8, 2024] |
| 7 | White spaces |
| 8 | Active nav link |




- I tried to create a function, that a separate user can add a review to any trip.
Since this app is working with mongo and is a non-relrional database there was an id key error.

- Date stamp format was not clear looking like this Added on: [7, 8, 2024] 

