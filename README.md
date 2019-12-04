## Project - Full-Stack Development
### Muay Thai Personal Training

#### <u>Summary</u>

Interested parties of the public interested in combat sport may be intimidated by violence, injuries and all the negative impressions portrayed by combat sports events and sometimes gyms themselves in their marketing material.

The idea is to alter that image with a different perception that everyone should be practising and gaining from Muay Thai as a form of art and culture, instead of trying to be the best fighter in town. This project depicts a solution to that problem by providing specialised and personalised services. 

This is an E-Commerce website designed to be used by a business to host a website for Free-Lance Personal Training specialising in teaching the combat sport, Muay Thai. Users will be able to purchase different types of services, which are essentially training sessions catering to individual needs and goals. 

#### <u>How it works</u>

Users can create an account on the website or login to an existing account. Before they are logged in, they will be able to access the shop page to view the products offered before creating an account. The Landing Page will also provide basic information on what to expect from the services provided by providing a description. 

After creating an account and logging in, more shop information will be revealed.  After logging in, they will also be able to gain access to make purchases. For example, logged in users can add items from the shop into their basket. From the basket page, they can adjust the quantity or delete the basket item altogether. While adjusting the quantity, the total amount due displayed will update accordingly. Discounts are offered based on a number of properties of the purchase being made. Once the user is ready to make payment, he/she will go to the next page and enter their order details and card details. Card details are kept completely private and sent straight to Stripe Payment.

After creating their account, users can also access their order history and will be able to edit their own profile if they wanted to make adjustments from the original registration process.

The live version of this website can be found [here](www.sgmuaythai.org).

The herokuapp version can be found [here](https://sgmuaythai.herokuapp.com/).

( ***For CI examiners*** : you may opt to use the following details during the testing process, a password reset will require a separate legitimate email to receive the reset link. 


*typical user*
**username**: benwyatt
**password**: benny111
**valid 10%-off discount codes**: I7BEe9VYeM, xzrlfaQzoB, tRfcZDL3Jg

*admin user*
**username**: ronswanson
**password**: ronny111

Note: Because the Administrator Page is not visible to customers or the public, the functionality of the page was prioritised over the UI/UX, mobile responsiveness and frontend development for this project.
)

#### Testing

Manual Testing was conducted and the documentation can be found [on github](https://github.com/jaymanmt/PMT) in a pdf file.


#### UI/UX - 5layers

##### <u>Strategy</u>

PMT is a E-Commerce website aimed to provide personal training services in the form of muay thai. Such Personal Training services are very rare and only available in gyms that already provide a range of group classes including ones specialising in muay thai. Most gym members will not purchase these personal training sessions since are already paying a monthly fee to be in the gym. Therefore, this service which focuses solely on affordable one-to-one training in muay thai makes it unique as it attracts non-current gym members. 

User 1 Story: "I love watching combat sports and find it scary. Everytime I pass by a gym, I am confronted at the idea of getting injured or beat up since I have no experience in martial arts."

User 2 Story: "I find martial arts gyms scary and confronting since I have no experience whatsoever."

User 3 Story: "I have joined a martial arts gym before but did not get much attention and adopted some bad technique which I find hard to shake off. I'm not sure what muay thai actually is."

User 4 Story: "My kids are so hyperactive that I don't know what to do with them. Taekwondo and Karate seem overly mainstream and not very effective as a form of self-defence for them."

This website's services provides the solution to members of the public who either have had bad experiences in martial arts gyms or are confronted by the idea of pursuing combat sports. 

##### <u>Scope</u>

###### Functional Requirements:

Able to create accounts, reset password, add items to basket, make purchases, access and edit profile, access order history, logout. 

**Create Account**: Register with a valid email to create an account, that will gain access to being able to add items to the individual's basket/cart. 

**Shop**: Shop is accessible without having  to create to account to give viewer's an idea of what can be purchased and if the services provided suit their interest or needs before having to create an account. 

**Basket**: Items added to the basket will stay in the basket persistently. Adding over 5 items to the basket will result in a 10% discount from the total bill. 

**Payment**: Payment is powered by Stripe to protect user's payment information. Stripe will protect against invalid card details. Payment will not be allowed if the basket is empty or the transaction created does NOT have the status of 'PENDING'. 10% discount already applied if 5 packages and above purchased. Additional 10% off with use of an active discount code. 

**Edit Profile**: A feature provided for users who might want to update essential details especially after purchase so that they can describe to the service provider a little more about themselves such as injuries or additional information such as travel or schedule limitations. Additional information always contributes to improving overall results for the customers. 

**Order History**: Enables users who have made payment have a sense of reassurance that there is a record of their purchase and its current status. 

**Email**: Email sent to customer once purchase has been made to confirm the order. Email also sent to the aministrator's personal email account to alert him/her. 

**Logout**: User can log out of their accounts.

**Administrator Page**: Admin users can update edit existing shop items, add new shop items, edit user profiles, update individual transaction status. Administrators can still make purchases for testing purposes. 

###### Content Requirements:

In order to load the functional components, database entities include:
1) Each User's account information
2) Transaction Details,
3) Charge Details for each transaction that has been paid for
4) Invoice Items to record each item in each transaction and the quantity purchased.
5) Referral Codes to store unique referral codes.
6) Basket entity to store individual users' cart items. 
7) Item to store  shop items and their individual details.
8) Categories to better organise types of Shop Items

##### <u>Structure</u>

Important and frequently accessed items such as the shop and basket are accessible directly via icons while other features such as order history and password reset are found in a dropdown menu from the navbar. 

State Changes such as invalid mobile numbers are signaled across the top below the navbar to inform the user that an error has occurred. At the same time, when information has been processed successfully, the user is either informed via those message tabs across the top or redirected to another page such as the 'thank you' page after payment has been processed. 

##### <u>Skeleton</u>

Struture of the website follows a similar approach to a typical e-commerce website, where the navbar is located up the top. Shop items spaced out evenly. Profile, Basket and Payment pages are centralised on the page for easy reading, mobile responsiveness and thus, smoother item selection and payment process. 

A wireframe for structure was not used for this website as the structure of the webpage follows a simple e-Commerce layout. 

##### <u>Surface</u>

White-ish background with darkened undertones to represent a form of elegancy through out website. Stuck with 5 color themes throughout, red, yellow, black and white.
Used translucent background with white font color to present a minimalistic approach in the navbar and forms. 


#### Features 

1) Login, Logout
2) Register an account
3) Add items to basket
4) Make purchase for items in basket
5) Sends email to administrator and customer
6) Display order history
7) Administrator has ability to visualise useful data and search for specific users
8) Administrator has ability to delete users, edit users, add new shop items, edit existing shop items, update transaction status. 

***Features left to implement***:

- Add more types of discount codes
- Ability to send newsletters via admin page

#### Technologies Used

- HTML
- CSS
- JAVASCRIPT and JQUERY
- PYTHON
- DJANGO
- S3 (database)
- Mailgun (email)
- STRIPE (payment)
- BOOTSTRAP 4.3
- GitHub (Version Control)
- Heroku (deployment)
- POSTGRESSSQL (database relationship model)
- Cloud 9 (IDE Web Development Environemnt)
- Google Fonts

#### Deployment

Github repository named "PMT" was created for this project. Regular commits were made to display progress of the website over a period of time. The site is deployed directly from the Heroku App with an added domain name from NameCheap:
The live site can be found on [here](www.sgmuaythai.com).
The heroku app can be found [here](https://sgmuaythai.herokuapp.com)

The site is aimed not only to be a project but also as a live eCommerce site to provide specialised personal training services to the Singapore Public. Therefore, a git-branch is performed to continue working on the website while the project is being assessed.



#### Credits

Adding crispy forms attachment. [Link](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)

Setting customisable password reset form. [Link](https://wsvincent.com/django-user-authentication-tutorial-password-reset/)

Stipe Brand Assets. [Link](https://stripe.com/en-sg/newsroom/brand-assets)

Show images on Django. [Link](https://stackoverflow.com/questions/9498012/how-to-display-images-from-model-in-django)

Auto Upload profile photo for new user sign ups. Image gotten from [here](https://www.flaticon.com/authors/freepik)

Adding object filters by group. [Link](https://stackoverflow.com/questions/4789021/in-django-how-do-i-check-if-a-user-is-in-a-certain-group)

Sending emails from django using mailgun. [Link](https://madradavid.com/sending-email-django-and-mailgun/)

All icons gotten from Fontawesome. [Link](https://fontawesome.com/icons?d=gallery)

Food Photo by Pexels. [Link](https://www.pexels.com/)

Hero image and rest of photos gotten through licensed adobe stock photos. [Link](https://stock.adobe.com/sg/photos)