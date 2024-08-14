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

After the css test there remained i error this was an error i the materialize css, since the app is built using some materialize components, I had to add the link to the materialize cdn despite the error. The same appplies to the warnings returned by the css checker. Some of the warnings seem to come from my code, however the checker does not specify. Fter some research it turns out that the checker is a biy outdated and doies not support all modern css conventions.

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