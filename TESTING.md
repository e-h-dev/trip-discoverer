# Trip Discoverer - Testing

## Trip Discoverer app is responsive to all devices.

### Home Page
![Home Page](/assets/validation-images/responsive-images/home-page-responsive.png)

- - -

### Sign up Page

![Sign up page](/assets/validation-images/responsive-images/sign-up-responsive.png)


- - -

## CONTENTS
* [App responsivness](#trip-discoverer-app-is-responsive-to-all-devices)
* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [Lighthouse](#lighthouse)
* [JavaScript test](#jshint-java-script-test)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.

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

The css check came back with no errors, there are however some warnings the validator only gives the folowing message; `Due to their dynamic nature, CSS variables are currently not statically checked` the common denominator is, on all th elines that there is a warnong there is a (var) attribute leading to the root styles. After some research it turns out that the jigsaw checker is a bit outdated and does not support all modern css conventions.

![css checker](/assets/validation-images/html-css-checker/css-validation.png)

- - -

### Jshint Java Script test

 * My code is written using ES6 Javascript syntax. The let key word was flagged as a warning by jshint.
 * No other warnings were present.
 * script.js

 ![JavaScript test](/assets/validation-images/js-python-validation-images/js-validation.png)
 
 - - -

 ### Python linter test

 * After putting my app.py file to the linter test, it passed with no errors

 ![Python linter test](/assets/validation-images/js-python-validation-images/python-linter-validation.png)

 - - -

 ## Lighthouse valildation

 - All pages have been tested by lighthouse, and have passed all the criteria with a score above 90.

 ### Home page desktop

 ![Home page desktop](/assets/validation-images/lighthouse/trips-page-lighthouse.png)

 ### Home page mobile

 ![Home page mobile]()

 - - -

 ### Sign up page desktop

 ![Sign up page desktop](/assets/validation-images/lighthouse/sign-up-page.png)

 ### Sign up page mobile

 ![Sign up page mobile]()

 - - -

 ### Sign in page desktop

 ![Sign in desktop](/assets/validation-images/lighthouse/sign-in-page.png)

 ### Sign in page mobile

 ![Sign in page mobile]()

 - - -

 ### Add trip page desktop

 ![Add trip page desktop](/assets/validation-images/lighthouse/add-trip-page.png)

 ### Add trip page mobile

 ![Add trip page mobile]()

 - - -

 ### Edit trip page desktop

 ![Edit trip page desktop](/assets/validation-images/lighthouse/edit-trips-page.png)

 ### Edit trip page mobile

 ![Edit trip page mobile]()

 - - -

 ### Users page desktop

 ![Users page desktop](/assets/validation-images/lighthouse/users-page.png)

 ### Users page mobile

 ![Users page mobile](/assets/validation-images/lighthouse/users-page-mobile.png)

 - - -

 # Testing User Stories

## Website Owner Goals

| REF | Goals | How are they achieved? |
| :--- | :--- | :--- |
| 1 | We want the website to attract a new and wide range of users. | With a clear and easy to use interface, with clear instuctions and nav links. Users will be interested and attracted to using the web app. |
| 2 | We want an attractive website, where the information is clear, and easy to access. | Using a range of technologies the app is very easy to use and store data. |
| 3 | We want the users to have the ability of signing in, to add their own trip ideas. | A simple sign up page which takes user information and posts it to the data base, allows for easy access for any registered user, where they can add their own trip ideas. |
| 4 | We want to be able to collect data from all users, to find their preferential category of trips, and places they visit. | With good search functionality the site owner can easily find all information about any user, using the admin inly users page. |
| 5 | We want to be able to provide consumer habit information, to small local businesses, to promote their business to our users. | The site owner can easily collect all the relavant infoamation from all the users. |
| 6 | We want the app to be responsive to all devices. | BY using materialize and custom media queries the app is responsive to all devices. |

## Site Visitor Goals

 REF | Goals | How are they achieved? |
| :--- | :--- | :--- |
| 1 | I want to have access to clear details regarding all the trips detailed by the website. | Each trip is displayed clearly on the trip page, the main information is first dispalyed and whe ckicked on the disaply box toggles down, to reveal a large array of inforamation about the trip. |
| 2 | I want to be able to easily search for my preferred trip, by location and category. | A simple search bar allows the user to search for anytihng wanted, from region to city to reviews and much more. The filter will also filter down the categories narrowing down the user's search.  |
| 3 | I want to add my own trip ideas to the website's database. | Once signed in the user can easiy click on the add trip nav link, and add a trip by filling in and submiting the form. |
| 4 | I want to be able to edit my trip ideas on the website's database. | When signed in the user can look at their trips, there is an option to both edit and delete their trips. |
| 5 | I want the site to be responsive to my device. | By using materialize and custom media queries the app is responsive to all devices. |
| 6 | I want the app to be easy to navigate. | Clear nav links with hover status and active class makes the app vary simpla and intuitive to navigate. |

- - -

## Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Lenovo
  * HP
* Mobile Devices:
  * Android Tablet

Each device tested the site using the following browsers:

* Google Chrome
* Microsoft Edge
* Opera

Additional testing was taken by friends and family on a variety of devices and screen sizes. They reported no issues whilst using the app.

- - -

## Manuel testing 

### Home Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


