# Rage Room - Booking System   
#### Hackathon 3 - Full Stack Project   

![Image of desktop home page wireframe](static/images/Web%201920%20–%201.png)

#### Summary  
The Rage Room website aims to bring an intuitive experience to their customers. The customers will have the option to view the upcoming events and register to the site in order to book themselves in and keep track of their upcoming events. The staff members will be able to access the event creation and editing features to ensure that the events stay up-to-date.  

#### User Persona  
- 25 to 45 years old
- Professional
- In need of a place to vent their frustrations  

#### Specification   
In order to deliver this project we will need to create a booking system with full CRUD functionality.  
This will be achieved by creating 3 models; UserProfile, RageRoomSession, BookingModel.  
These event and booking models will allow us to create a event creation and edit form. We will also have the ability to create a booking form for the average user / customer.  
The event creation and edit form will only be available to staff / admin while the event booking features will be available to all of our registered users.  
We will be using an agile workflow in order to achieve our vision - utlising a kanban board with our user stories to keep track of progress. Each day will start with a stand-up and end with a stand-down so that all team members are up-to-date and any blockers are addressed.

#### Ideation
We are working on setting up a user model for our website. This model needs to handle different kinds of users: from the big bosses to the regular folks just browsing. Django's got a user model already, but it might not be enough, so we are thinking of adding some tweaks to make sure everyone gets the right permissions.  

Then there's the Event Model. This is where all the action happens. It's going to need spaces for the basic stuff like what the event is called, what it's about, when and where it's happening, and who's running the show. All that's going to connect back to whoever's signed up on the site.  

Next up is the Booking Model. This one keeps track of who's signed up for what event. It needs to hook up to both the Event and User models. We will need to keep an eye on when someone books something and whether it's confirmed or not.  
We have also got to make sure the website knows who's who when users log in. This means setting up a system that makes sure everyone's who they say they are and can do only what they're supposed to do on the site.  

For signing up, making events, and booking them, we need to create some forms. Good thing Django has a tool for that which we plan to use. It should make this part easier.  
Then there's creating views. This is about making sure there's a place for everything on the site: adding events, changing them, or even getting rid of them if needed. And we can't forget about making sure users can sign up, log in, and manage their profiles easily.  

While working on the functionality of the website, we also took this time to develop our wireframes. The site's design will be simple in order to allow us to concentrate on the functionality. The colour scheme is inspired by nature. Many animals, when threatened, display strong and contrasting colours to warn all those around. To show they are frustrated and scared. A rage room is for those who need to vent frustration - to let out their inner animal.  

#### Design
![Image of desktop home page wireframe](static/images/Web%201920%20–%201.png)
![Image of desktop event list page wireframe](static/images/Web%201920%20–%208.png)
![Image of phone home page wireframe](static/images/iPhone%2014,%2013,%2012%20–%201.png)
![Image of phone event list page wireframe](static/images/Web%201920%20–%208.png)
  
    
## Day 1 
#### Targets
- Set up project models
- Connect project urls
- Finish wireframes
- Set up project kanban board
- Begin working on page templates
- Deploy

#### Issues
- User model issues: Connecting our user models across the different file paths proved to be difficult. 
  
- Design issues: In order to achieve the different background colours for our event's list, we will be implementing Django's cycle tag in the for loop. This is something that we have not tried before so will be interesting to see the outcome.  
Another design issues is the behaviour of our navigation on small screens - the content has been centered in a strange way. This will be solved by adjusting the alignment.

- General set up: As with all Django projects, the initial set up takes a while. This process was exacerbated by the mutliple team members. However, thanks to great leadership, communication, and determination the issues were solved efficiently. These issues mainly revolved around installing the correct packages, adding said packages to the requirements.txt file, ensuring every member had a env.py file set up with the correct links etc.   


## Day 2
#### Targets
- Build up the majority of the website
- Add style to website: Forms, Event List, Home Page, etc
- Begin Testing 
- Bug hunting
- Deploy

#### Issues
Design issues:
- Footer placement. On the majority of our pages, our footer did not stick to the bottom. For larger screens, this has been fixed by adjusting the min-height of the main element and then adjusting each page's height accordingly.  

- Deployment issues - In order for the project to deploy to Heroku, we must ensure that all requirements are included in our requirements.txt and the static files have been collected. Cloudinary has also been set up.

#### Tests
- Forms. In order for the site to have complete CRUD functionality our event forms need to be working. The main issue we are facing is that the events in the event list arent cooperating unless their capacity is set to 10. The forms are also being affected by the footer issue which is stopping interaction with the buttons. The buttons will be fixed by adjusting the relevant screen heights for all necessary breakpoints.  

- Links. All links in the navbar apart from the gallery are currently taking the user to the correct location. The gallery link will be working once the gallery page is set up and the url path is in place. The active class has not been showing up correctly on each page. This was fixed by changing the active class based on the current url pattern.  


## Day 3  
#### Targets  
- Finish update bookings page
- Fix all footer issues
- View event details modal. View events option available to customers and unregistered guests.
- Finish about page  
- Finish gallery page  
- Code validation
- Full test 
- Code housekeeping 
- Final deployment
- Presentation 