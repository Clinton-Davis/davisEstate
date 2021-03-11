# Davis Estates

Davis Estates is a fake real estate website where you can look and search for listed propertys for sale.

---

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7b4f76ae857f4e60886cdeea68c90761)](https://www.codacy.com/gh/Clinton-Davis/davisEstate/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Clinton-Davis/davisEstate&utm_campaign=Badge_Grade)

<!-- [![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco) [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master) [![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard) -->

## Motivation

My motivation behind the creation of Davis Estates was practice using Django and building up my portfolio and have a example to show future clients.

## UX

The idea was to make a fully functioning real estate website, where cliets could brouws for a potenctial new house, have a look at all the details, and contact a agent if they where interested.

### Scope

- Manage listings, realtors, contact inquiries and website users via admin
- Role based users (staff and non-staff)
- Display listings in app with pagination
- Ability to set listings to unpublished
- Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
- List realtors on about page with “seller of the month” (Control via admin)
- Listing page should have fields listed below
- Listing page should have 1 main image and 6 inner images with (if avaiable) floorplans using lightbox
- Lightbox should scroll through images
- Listing page should have a form to submit Enquiries for that property listing
- Form info should go to database and notify agent(s) with an email
- Frontend register/login to track inquiries
- Both unregistered and registered users can submit form. If registered, can only submit one per listing

### Structure

##### Home

The home page or Index page is the first page users see and can interact with. It is divided into 3 sections.

**Section 1**
Full page image with a light gray overlay that holdes the search form.

**Section 2**
Hold 3 of the newsest listing on the webpage.

**Section 3**
Hold information regarding the

- Consulting Services
- Property Management
- Renting & Selling

##### About

The About page holds all the details about Davis-Estates
This is where you will find the "Seller Of The Month". There is there picture and bio.

##### Listing

Here are all the listing we have to offer. They are in a "Card" format with three in a row with 6 to a page.
each listing has the price, a image, address, city and countie.
Followed by the number of Bedrooms, Bathrooms, if there is parking and square meters, as wel as the date it was listed.
At the bottom of the card is a 'More Info' button to take you to the listing details page.

##### Listing Details

The listing detials page has all the images of the listing and the agent that is looking after it.
There is more info about the listing here with a detialed description, and a google maps on the address.
Hear is where you can contact the agent to make an Enquiries about the listing.

##### Search

If you search for a listing, you wikk be taken to the search page, it has the same layout as the lising page, but will only show listing what have the criteria you searched for.

##### Register

The register page is a simple form that askes for emial address, username and Password, after a successfull registen the user is logged in automatily.

##### Login

The login form askes for the username and password, then if login is successfull the user is redirected to the home page.
**Dashboard**

### Surface

#### Colour Scheme

- ![#183f7e](https://placehold.it/15/183f7e/000000?text=+) `#183f7e` - Primary
- ![#303aca](https://placehold.it/15/303aca/000000?text=+) `#303aca` - Secondary
- ![#333333cc](https://placehold.it/15/333333cc/000000?text=+) `#333333cc` - Supplementary colour 1
- ![#17a2b8](https://placehold.it/15/17a2b8/000000?text=+) `#17a2b8` - Supplementary colour 2
- ![#e9464688](https://placehold.it/15/e9464688/000000?text=+) `#e9464688` - Supplementary colour 3
- ![#ffc10788](https://placehold.it/15/ffc10788/000000?text=+) `#ffc10788` - Supplementary colour 4
- ![#0bf76d88](https://placehold.it/15/0bf76d88/000000?text=+) `#0bf76d88` - Supplementary colour 4

---

## Technologies

### Core Languages, Frameworks, Editors

- [HTML 5](https://en.wikipedia.org/wiki/HTML) ~ Markup language designed to be displayed in a web browser.
- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) ~ Style sheet language used for describing the presentation of a document in HTML.
- [Python 3.8](https://code.jquery.com/) ~ High-level, general-purpose programming language.
- [Django 3.1.7](https://www.djangoproject.com/) ~ Django is a high-level Python Web framework.
- [Bootstrap 4.5](https://getbootstrap.com/) ~ Design and customize responsive mobile-first sites.
- [Heroku](https://heroku.com) ~ A cloud based platform - as a service enabling deployment of CRUD applications
- [Heroku Postgres](https://www.heroku.com/postgres) ~ PostgreSQL's capabilities - as a fast, functional, and powerful data resource.

#### Third-Party Tools

- [Visual Studio Code](https://code.visualstudio.com/) ~ Code editor redefined and optimized for building and debugging modern web and cloud applications.
- [GitHub](https://github.com/) ~ Distributed version control and source code management (SCM) functionality of Git, plus its own features.
- [Travis](https://travis-ci.org/) ~ Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket.
- [Font Awesome](https://fontawesome.com/) ~ Font Awesome icons

- [Git](https://git-scm.com/) ~ Distributed version control system
- [Slack](https://slack.com/intl/en-ie/) ~ A workspaces allowing you to organize communications by channels for group discussions and allows for private messages to share information.
- [autopep8](https://pypi.org/project/autopep8/) ~ A tool that automatically formats Python code to conform to the PEP 8 style guide
- [Codacy](https://app.codacy.com/) ~ Automated Code Review
- [TinyPNG](https://tinypng.com/) ~ A smart lossy compression technique to reduce the file size of your PNG files.
- [Google Fonts](https://fonts.google.com/) ~ A library free licensed font families, an interactive web directory for browsing the library.

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## Features

- The admin user may manage listings, agents, users and contact inquiries from the admin area.
- Staff members may login to the admin area whale normal users many but may login.
- Pagination is at 6 listing per page
- The staff members have the ability to set listings to unpublished if they would like to take it off the market.
- Users may search listings by keyword, city, state, bedrooms and price from the Homepage & search page.
- A list of agents are on the about page with “seller of the month” that is controled via admin area.
- Listing details page has all the data about the house listed below.
- Listing details page has 8 images, 1 main image and 6 interior images with 2 for floor plan (if avalible) all connected by the lightbox.
- The Lightbox scrolls through images.
- The listing detial page has a form that can be submited to inquire about a property listing.
- The inquire is saved to the database and the agent looking after the listing is notify via email.
- Both unregistered and registered users can submit form. If registered, can only submit one per listing.

## Deployment

### Local Deployment

To be able to clone this project there are a few things you will need.

- [Git](https://git-scm.com/) - Install Git, installation docs and be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Pip](https://pip.pypa.io/en/stable/installing/) - install pip, installation docs can be found [here](https://pip.pypa.io/en/stable/installing/)
- A [Gmail](https://www.gmail.com/mail/help/intl/en/about.html?utm_expid=...) account with app secret key.

Once you have [Git](https://git-scm.com/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed.

1. From the terminal create the directory you want to work in.

   ```bash
   $ mkdir <filename>
   ```

2. Change into Directory

   ```bash
   $ cd <filename>
   ```

3. Clone the repository from github.

   ```bash
   $ git clone https://github.com/Clinton-Davis/davisEstate.git
   ```

4. Change into focus_fitness directory.

   ```bash

   $ cd destates
   ```

5. Install [virtualenv](https://pypi.org/project/virtualenv/)

   ```bash

   $ pip install virtualenv
   ```

6. Create a virtual environment (env)

   ```bash
   $ virtualenv env
   ```

7. Activate env with:

   ```bash
   $ source env/Scripts/activate
   ```

8. In focus folder make a `.env` file and add the variables below.

   > There is a handy .templates.env file with all the variables.

   | Key                |      Value      |
   | ------------------ | :-------------: |
   | SECRET_KEY         | < Your Values > |
   | EMAIL_HOST_PASS    | < Your Values > |
   | EMAIL_HOST_USER    | < Your Values > |
   | NOTIFY_EMAIL       | < Your Values > |
   | DEFAULT_FROM_EMAIL | < Your Values > |

9. Install all the requirements needed to run the project.

   ```bash

   $ pip install -r requirements.txt
   ```

10. Then migrate

    ```bash

    $ python manage.py migrate
    ```

11. Create superuser.

    ```bash

    $ python manage.py createsuperuser
    ```

12. Load agents.

    ```bash

    $ python manage.py loaddata agents.json
    ```

13. Load Listings.

    ```bash

    $ python manage.py loaddata listings.json
    ```

14. Run project with

    ```bash

    $ python manage.py runserver
    ```

 <div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## Tests

Describe and show how to run the tests with code examples.

## How to use?

If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Credits

giving to me by Brad Traversy.
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project.

#### Anything else that seems useful

## License

A short snippet describing the license (MIT, Apache etc)

MIT © [ClintonDavis]()
