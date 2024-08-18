# Trip Discoverer - Testing

## Trip Discoverer app is responsive to all devices.

### Home Page
![Home Page](/assets/validation-images/responsive-images/home-page-responsive.png)

- - -

### Sign up Page

![Sign up page](/assets/validation-images/responsive-images/sign-up-responsive.png)

- - -

### Add trip Page

![Add trip page](/assets/validation-images/responsive-images/add-trip-responsive.png)

- - -

### Users Page

![Users page](/assets/validation-images/responsive-images/users-page-responsive.png)

- - -

## CONTENTS
* [App responsivness](#trip-discoverer-app-is-responsive-to-all-devices)
* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
* [JavaScript test](#jshint-java-script-test)
* [Full Testing](#full-testing)
  * [Testing User Stories](#testing-user-stories)
  * [MANUAL TESTING](#manual-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building, to pinpoint and troubleshoot any issues as I went along.

During development I made use of google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I have gone through each page using google chrome developer tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

I used [W3C Validator](https://validator.w3.org/) to validate the HTML on all pages of the website.

I used [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate the CSS file.

### Home page

![Home page validation](/assets/validation-images/html-css-checker/trips-page-validation.png)

### Sign up page

![Sign up page validation](/assets/validation-images/html-css-checker/sign-up-page-validation.png)

- - -

### Sign in page

![Sign in page validation](/assets/validation-images/html-css-checker/sign-in-page-validation.png)

- - -

### Add trip page

![Add trip page validation](/assets/validation-images/html-css-checker/add-trip-page-validation.png)

- - -

### Edit trip page

![Edit trip page validation](/assets/validation-images/html-css-checker/edit-trip-page-validation.png)

- - -

### Users page

![Users page validation](/assets/validation-images/html-css-checker/user-page-validation.png)

- - -

### CSS checker

The css check came back with no errors, there are however some warnings the validator only gives the following message; `Due to their dynamic nature, CSS variables are currently not statically checked` the common denominator is, on all the lines that there is a warning there is a (var) attribute leading to the root styles. After some research it turns out that the jigsaw checker is a bit outdated and does not support all modern css conventions.

![css checker](/assets/validation-images/html-css-checker/css-validation.png)

- - -

### Jshint Java Script test

 * My code is written using ES6 JavaScript syntax. The let key word was flagged as a warning by jshint.
 * No other warnings were present.
 * script.js

 ![JavaScript test](/assets/validation-images/js-python-validation-images/js-validation.png)
 
 - - -

 ### Python linter test

 * After putting my app.py file to the linter test, it passed with no errors

 ![Python linter test](/assets/validation-images/js-python-validation-images/python-linter-validation.png)

 - - -

 ## Lighthouse validation

 - All pages have been tested by lighthouse and have passed all the criteria with a score above 90.

 ### Home page 

 ![Home page](/assets/validation-images/lighthouse/trips-page-lighthouse.png)


 - - -

 ### Sign up page 

 ![Sign up page](/assets/validation-images/lighthouse/sign-up-page.png)


 - - -

 ### Sign in page 

 ![Sign in](/assets/validation-images/lighthouse/sign-in-page.png)


 - - -

 ### Add trip page 

 ![Add trip page](/assets/validation-images/lighthouse/add-trip-page.png)

 - - -

 ### Edit trip page 

 ![Edit trip page](/assets/validation-images/lighthouse/edit-trips-page.png)


 - - -

 ### Users page 

 ![Users page](/assets/validation-images/lighthouse/users-page.png)


 - - -

 # Testing User Stories

## Website Owner Goals

* Note the reference in the left column, corresponds to the [Goals images](#goal-images) below.

| REF | Goals | How are they achieved? |
| :--- | :--- | :--- |
| A | We want the website to attract a new and wide range of users. | With a clear and easy to use interface, with clear instructions and nav links. Users will be interested in using the web app and will find it attractive. |
| B | We want an attractive website, where the information is clear, and easy to access. | Using a range of technologies the app is extremely easy to use and store data. |
| C | We want the users to have the ability of signing in, to add their own trip ideas. | A simple sign-up page which takes user information and posts it to the data base, allows for easy access for any registered user, where they can add their own trip ideas. |
| D | We want to be able to collect data from all users, to find their preferential category of trips, and places they visit. | With good search functionality, the site owner can easily find all information about any user, using the admin only users page. |
| E | We want to be able to provide consumer habit information, to small local businesses, to promote their business to our users. | The site owner can easily collect all the relevant information from all users. |
| F | We want the app to be responsive to all devices. | By using materialize, and custom media queries the app is responsive to all devices. |

## Site Visitor Goals

 REF | Goals | How are they achieved? |
| :--- | :--- | :--- |
| G | I want to have access to clear details regarding all the trips detailed by the website. | Each trip is displayed clearly on the trip page, the main information is first displayed and when clicked on the display box toggles down, to reveal a large array of information about the trip. |
| H | I want to be able to easily search for my preferred trip, by location and category. | A simple search bar allows the user to search for anything wanted, from region, to city, to reviews, and much more. The filter will also filter down the categories narrowing down the user's search.  |
| I | I want to add my own trip ideas to the website's database. | Once signed in, the user can select the add trip nav link and add a trip by filling in and submitting the form. |
| J | I want to be able to edit my trip ideas on the website's database. | When signed in the user can look at their trips, there is an option to both edit and delete their trips. |
| K | I want the site to be responsive to my device. | By using materialize and custom media queries the app is responsive to all devices. |
| L | I want the app to be easy to navigate. | Clear nav links with hover status and an active class, makes the app simple and intuitive to navigate. |

### Goal images

## A.

![image of clear navigation](/assets/page-images/home-page.png)

## B.

![gif showing trip information scroll down](/assets/testing-gifs/goal-b.gif)

## C.

![gif for sign in](/assets/testing-gifs/goal-c.gif)

## D.
![gif for search users](/assets/testing-gifs/goal-d.gif)

## F.

![Responsive Pages](/assets/validation-images/responsive-images/home-page-responsive.png)

## G.

![gif showing trip information scroll down](/assets/testing-gifs/goal-b.gif)

## H.

![Search for trip](/assets/testing-gifs/goal-h.gif)

## I.

![Add trip gif](/assets/testing-gifs/goal-i.gif)

## j.

![Edit trip gif](/assets/testing-gifs/goal-j-1.gif)


![Delete trip giff](/assets/testing-gifs/goal-j-2.gif)




- - -

## Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Lenovo
  * HP
* Mobile Devices:
  * Android Tablet

Each device assessed the site using the following browsers:

* Google Chrome
* Microsoft Edge
* Opera

Additional testing was taken by friends and family, on a variety of devices and screen sizes. They reported no issues whilst using the app.

- - -

## Manual testing 

### Home Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Sign in link. | Link to Sign in page. | Clicked on link. | Sign in page loads. | Pass |
| Sign up link. | Link to Sign up page. | Clicked on link | Sign up page loads. | Pass |
| Add trip link. | Link to Add trip page (When user in session). | Clicked on link. | Add trip page loads. | Pass |
| Users link (Admin only). | Link to Users page (When admin in session). | Clicked on link. | Users page loads | Pass |
| Mobile nav links hamburger. | Toggles open nav bar on mobile devices. | Clicked on hamburger icon. | Side nav bar toggles open. | Pass |
| Search bar. | User can type in search request, the page will only load searched for trips. | Type in search request. | Only searched for trips loaded on trips page. | Pass |
| Filter. | Click on any of the categories in the filter section, only trips from that category (or have criteria from category) will load. | Click on a filter button. | Only that category loads. | Pass |
| Display boxes | All trips should be displayed on the trips (home) page, in display boxes. | Page loaded. | All the trips are displayed in separate display boxes. | Pass |
| Rating stars | Number of stars to show on display box, should correspond to rating number user puts into the input form. | Added trips with varying rating results. | Rating displayed, corresponds the number user put in the form. | Pass |
| Website link | Weblink button should open trip's website on another tab. | Clicked on web button. | New tab opened with trip's website. | Pass |
| Edit link | User should be able to edit trip, when clicking on edit trip button. | Clicked on edit trip button. | Edit trip form opens. | Pass |
| Delete request button | When clicking on Delete trip button, a message should show with option to delete or cancel delete. | Clicked on delete button. | Delete message shows. | Pass |
| Cancel delete button | After clicking on delete button, cancel button should stop delete and reload page. | Clicked on cancel button. | Delete is cancelled, and page reloads. | Pass |
| Delete button | Deletes trip. | Clicked on delete button. | Trip Deleted. | Pass |
| Back to top scrolling button | When scrolling down the page, a button should appear. | Scrolled down page. | Button appeared. | Pass |
| Back up button | Clicking on the button, should scroll page back to top. | Clicked on the button. | Page scrolled back to top. | Pass |


- - -

### Sign up Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Sign in link. | Link to Sign in page. | Clicked on link. | Sign in page loads. | Pass |
| Sign up link. | Link to Sign up page. | Clicked on link | Sign up page loads. | Pass |
| Mobile nav links hamburger. | Toggles open nav bar on mobile devices. | Clicked on hamburger icon. | Side nav toggles open. | Pass |
| Sign up form. | When loaded the page should have a form, which user information can be put in. | On page load form appears. | User information can be added. | Pass |
| Sign up button. | When clicking on sign up button user should be added to data base and be signed in. | Clicked on sign up button. | User was added to data base and signed in. | Pass |
| Back to top scrolling button | When scrolling down the page, a button should appear. | Scrolled down page. | Button appeared. | Pass |
| Back up button | Clicking on the button, should scroll page back to top. | Clicked on the button. | Page scrolled back to top. | Pass |
- - -

### Sign in Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Sign in link. | Link to Sign in page. | Clicked on link. | Sign in page loads. | Pass |
| Sign up link. | Link to Sign up page. | Clicked on link | Sign up page loads. | Pass |
| Sign in form. | When loaded the page should have a form, which user information can be put in. | On page load form appears | User information can be added. | Pass |
| Sign in button. | When clicking on sign in button, user should be signed in. | Clicked on sign in button. | User was signed in. | Pass |

 - - -

 ### Add trip Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Add trip link. | Link to Add trip page (When user in session). | Clicked on link. | Add trip page loads. | Pass |
| Users link (Admin only). | Link to Users page (When admin in session). | Clicked on link. | Users page loads | Pass |
| Mobile nav links hamburger. | Toggles open nav bar on mobile devices. | Clicked on hamburger icon. | Side nav toggles open. | Pass |
| Add trip form. | When loaded the page should have a form, where user can put in trip information. | On page load form appears. | Trip information can be added. | Pass |
| Submit button. | When clicking on submit button, trip should be added to data base and trips page display. | Clicked on submit button. | Trip was added. | Pass |
| Back to top scrolling button | When scrolling down the page, a button should appear. | Scrolled down page. | Button appeared. | Pass |
| Back up button | Clicking on the button, should scroll page back to top. | Clicked on the button. | Page scrolled back to top. | Pass |
 - - -

 ### Edit trip Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Add trip link. | Link to Add trip page (When user in session). | Clicked on link. | Add trip page loads. | Pass |
| Users link (Admin only). | Link to Users page (When admin in session). | Clicked on link. | Users page loads | Pass |
| Mobile nav links hamburger. | Toggles open nav bar on mobile devices. | Clicked on hamburger icon. | Side nav toggles open. | Pass |
| Edit trip form. | When loaded the page should have a form, which user can edit trip information. | On page load edit form appears. | Trip information can be edited. | Pass |
| Submit button. | When clicking on submit button, trip should be updated to data base and trips page display. | Clicked on add trip button. | Trip added. | Pass |
| Cancel Button | When clicking on cancel button, trip edit should cancel, and trips page reload. | Clicked on cancel button. | Trip edit cancelled and trips page reloaded. | Pass |
| Back to top scrolling button | When scrolling down the page, a button should appear. | Scrolled down page. | Button appeared. | Pass |
| Back up button | Clicking on the button, should scroll page back to top. | Clicked on the button. | Page scrolled back to top. | Pass |
- - -

### Users Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home logo. | Link back to home page. | Clicked on logo. | Home page reloads. | Pass |
| Home link. | Link back to home page. | Clicked on Home link. | Home page reloads. | Pass |
| Add trip link. | Link to Add trip page (When user in session). | Clicked on link. | Add trip page loads. | Pass |
| Users link (Admin only). | Link to Users page (When admin in session). | Clicked on link. | Users page loads | Pass |
| Mobile nav links hamburger. | Toggles open nav bar on mobile devices. | Clicked on hamburger icon. | Side nav toggles open. | Pass |
| Users display boxes | When users page loads all registered users should be displayed in boxes. | Opened users page. | All registered users displayed. | Pass |
| Search user button | On user display box search button should load all trips added by the user. | Clicked on search user button. | All user's trips displayed. | Pass |
| Delete user button | Delete user button on display box should delete user from database. | Clicked on delete user button. | User deleted from database. | Pass |
| Back to top scrolling button | When scrolling down the page, a button should appear. | Scrolled down page. | Button appeared. | Pass |
| Back up button | Clicking on the button, should scroll page back to top. | Clicked on the button. | Page scrolled back to top. | Pass |


