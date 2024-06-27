# <div id="up">Dental Care</div>

![](documentation/am_i_responsive.png)

### [Live site](https://dental-clinic-alsona-51e44ef82e4f.herokuapp.com/)

## Contents:

- <a href="#ux">UX</a>
  - <a href="#strategy">Strategy</a>
  - <a href="#db">Database structure</a>
  - <a href="#design">Design</a>
  - <a href="#wireframes">Wireframes</a>
- <a href="#testing">Testing</a>
- <a href="#bugs">Bugs</a>
- <a href="#features">Existing Features</a>
- <a href="#f_features">Features left to Implement</a>
- <a href="#technology">Languages, Technologies & Libraries</a>
- <a href="#credits">Credits</a>
- <a href="#deployment">Deployment</a>
- <a href="#acknowledgements">Acknowledgements</a>

## <div id="ux">UX</div>
### Overview
Dental Care is a comprehensive website designed for anyone seeking a variety of dental services. Our clinic offers a wide range of treatments, including teeth whitening, orthodontics, implants, and fillers. Our experienced team includes three distinguished dentists: prosthodontists Felix Ellis and Paul Kefalas, and orthodontist Rosa Murphy. Patients can easily book appointments with the dentist of their choice.

In addition, the website features a convenient contact form for any questions or concerns you may have. Patients can also create an account to view their appointment history and manage upcoming appointments. Our goal is to make dental care as accessible and convenient as possible for everyone.

#### First Time User
- The user can contact the clinic for any question they might have.
- A user who is looking for clear information about the Dental Care clinic and services provided.
- A user who prefers to make bookings digitally rather than speaking with others.
- An overall information about the clinic. 

#### Returning User
- As a returning user, I would like to review all my previous dentist's appointments.
- As a returning user, who already has an account I would like quickly and easily make an appointment with a particular dentist.
- As a returning user, I would like to see updates to the information on the site, for example new prices or new services. 

### <div id="strategy">Strategy</div>
To determine the best approach, we focused on understanding the needs of our potential users. This involved ensuring they could log in, and quickly and easily perform all necessary actions, including booking, reading, updating, and deleting appointments (CRUD).

One of the standout features of our website is the ability to book appointments based on real-time availability with specific dentists. The booking form includes three dependent dropdown lists, allowing users to select the service they need, choose their preferred dentist, and pick a suitable date and time for their appointment.

#### Agile
The Agile methodology was used to plan the project. Github was used as the tool to demonstrate this. Milestones were used to create Epics. Each user story was linked to an Epic and placed within one of three Iterations. Issues were used to create User Stories with custom templates ([Link to Kanban board](https://github.com/users/alsona1188/projects/10/views/1)). 
To prioritize tasks [MoSCoW method](https://github.com/alsona1188/pp4-dental-clinic/issues?q=is%3Aissue+is%3Aclosed) was used.

#### User Stories 

Issues were used to create User Stories with custom templates for admin and user. I added the acceptance criteria and the tasks so I can track my work effectively. Once I completed a User Story I would move it from `in progress` to `completed`. 

- Completed User Stories:<br />

  - Epic: Enable users to CRUD the bookings.<br />

    - As a site user I can book an appointment so that I can have the service I want.
    - As a site user I can update my appointment so that I can change the details.
    - As a site user I can view my appointments so that I can keep track of them.
    - As a logged-in user I can to view my profile information so that I can see my appointment history.
    - As a site user I can click on the delete button so that cancel my appointment.

  - Epic: Enable users to create an account and log in. <br />

    - As a user I can log in so that I can access my profile.
    - As a site user I can create an account so that I can be able to interact with the website. <br/>

  - Epic: Enable unregistered users to view all the key information about the dental clinic. <br/>

    - As a site user I can examine the information on the home page about the services provided so that I can decide if i want to use them.
    - As a site user I can click on the about page so that read all the information. <br/>

  - Epic: Set up service and contact page. <br/>
    - As a site user I can click on the contact page so that I can read all the contact forms.
    - As a site user I can click on the service page so that I can read all the info about the services that are
offered. <br/>

  - Epic: Epic: Set up admin page for admin to manage the dental clinic. <br/>
    - As an admin I can have a CRUD access to database data so that I can make necessary changes.
    - As an admin I can view the appointments so that I can manage the doctor's timetable.
    - As an **admin user ** I can update the about page so that it is updated and available for the users. <br/>

- Uncompleted User Stories: <br/>

    The following User Stories were not completed (marked as `wont have` in MoSCoW method table) as they were deemed to be not necessary for this project at this time but are indications of possible future features:<br/> 

    - As a site user I can receive the confirmation email so that I can see my appointment.
    - As a site user I can edit my password so that change my profile data.
    - As a site user I can be able to click on the blog page so that I can see the content.

  ---

### <div id="db">Database structure</div>

![](documentation/dental_care_erd.png)

When I decided on my initial concept of this project I knew I needed to understand what type of data I would need to store and the relationships between them. I created a Database Schema to help guide me.

#### Relationships

- A Service can be provided by multiple Dentists, and a Dentist can offer multiple Services. (Many-to-Many)
- An AppointmentRequest is associated with a User, a Service, and a Dentist. (Many-to-One for each relation)
- An AvailableTimeSlot is associated with a Dentist. (Many-to-One)
- User model (from Django's auth system) is associated with AppointmentRequest.

#### Models and Fields
- Service
  - name: CharField
  - price: DecimalField
  - featured_image: CloudinaryField
  - description: TextField

- Dentist
  - first_name: CharField
  - last_name: CharField
  - specialty: CharField
  - services: ManyToManyField (related to Service)
  - featured_image: CloudinaryField

- ContactFormRequest
  - name: CharField
  - email: EmailField
  - subject: CharField
  - message: TextField
  - read: BooleanField

- About
  - title: CharField
  - updated_on: DateTimeField
  - content: TextField
  - featured_image: CloudinaryField

- AppointmentRequest
  - user: ForeignKey (related to User)
  - service: ForeignKey (related to Service)
  - dentist: ForeignKey (related to Dentist)
  - date: DateField
  - time: TimeField
  - message: TextField
  - read: BooleanField
  - created_at: DateTimeField

- AvailableTimeSlot
  - dentist: ForeignKey (related to Dentist)
  - date: DateField
  - time: TimeField


### <div id="design">Design</div>

The site design is intuitive and functional. The main goal of the site is to provide users with practical and useful information about the services and functionality for making an appointment, and in this context, purposeful efforts have been made, as well as focus on the views required by users.
The colours are chosen to convey the dental environment. They are specified on the style.css: 
  - :root {
    --primary: #06A3DA;
    --secondary: #F57E57;
    --light: #EEF9FF;
    --dark: #091E3E;
}

### <div id="wireframes">Wireframes</div> 

> home.html

![](documentation/home_page.png)

> about.html

![](documentation/about_page.png)

> contact.html

![](documentation/contact.png)

> appointment.html

![](documentation/make_appointment.png)

> appointment_list.html

![](documentation/appointments_list.png)

<a href="#up">Back to Top of page</a>

---
## <div id="testing">Testing</div>

### Manual testing
Thorough testing was conducted by the developer and multiple users among friends and family. Usability suggestions were considered and acted on.
All design features have been manually tested and everything functions as expected. Testing was completed in my local terminal and also in Heroku deployment.

- Testing for responsiveness was conducted using Chrome Dev Tools. The website was tested extensively on a range of emulated mobile, tablet and large format screen sizes in both portrait and landscape orientations.<a href="#responsiveness">(Testing results are here)</a>

- All HTML files were passed through the W3C validator with no errors.
- CSS file (`style.css`) was passed through the W3C validator with no errors.
- The website was tested on browsers Chrome, Firefox, Edge and Opera.
- All user flows were tested, including landing page navigation, link clicks and forms submissions.
- All forms have been tested to ensure they are validated and can be submitted without errors.

The steps and results are as follows.
