## Project - Full-Stack Development
### Muay Thai Personal Training

#### <u>Summary</u>

Interested parties of the public interested in combat sport may be intimidated by violence, injuries and all the negative impressions portrayed by combat sports events and sometimes gyms themselves in their marketing material.

The idea is to alter that image with a different perception that everyone should be practising and gaining from Muay Thai as a form of art and culture, instead of trying to be the best fighter in town. This is an project depicts a solution to that problem by providing services. 

This is an E-Commerce website designed to be used by a business to host a website for Free-Lance Personal Training specialising in teaching the combat sport, Muay Thai. Users will be able to purchase different types of products, which are essentially training sessions catering to individual needs and goals. 

#### <u>How it works</u>

Users can create an account on the website or login to an existing account. Before they are logged in, they will be able to access the shop page to view the products offered before creating an account. THe Landing Page will also provide basic information on what to expect from the services provided by providing a backdrop. 

After creating an account and logging in, more information will be revealed including a more personal profile and contact information of the training provider. After logging in, they will also be able to gain access to make purchases Users can add items from the shop into their basket. From the basket page, they can adjust the quantity or delete the item altogether. While adjusting the quantity, the total amount due will update accordingly. Discounts are offered based on a number of properties of the purchase. Once the user is ready to make payment, he/she will go to the next page and enter their order details and card details. Card details are kept completely private and sent straight to Stripe Payment.

After creating their account, users can also access their order history and will be able to edit their own profile if they wanted to make adjustments.

A live version can be found [here]().

#### Testing

Testing was conducted and the documentation can be found [here]().


#### UI/UX - 5layers

##### <u>Strategy</u>

PMT is a E-Commerce website aimed to provide personal training services in the form of muay thai. Such Personal Training services are very rare and only available in gyms that already provide group classes. Most gym members will not purchase these personal training sessions since are already paying a monthly fee to be in the gym. Therefore this service which focuses solely on affordable one-to-one training in muay thai makes it unique in itself. 

User 1 Story: "I love watching combat sports and find it scary. Everytime I pass by a gym, I am confronted at the idea of getting injured or beat up since I have no experience in martial arts."

User 2 Story: "I find martial arts gyms scary and confronting since I have no experience."

User 3 Story: "I have joined a martial arts gym before but did not get much attention and adopted some bad technique which I find hard to shake off. I'm not sure what muay thai actually is."

User 4 Story: "My kids are so hyperactive that I don't know what to do with them. Taekwondo and Karate seem overly mainstream and non-effective as self-defence for them."

This website's services provides the solution to members of the public who either have had bad experiences in martial arts gyms or are confronted by the idea of pursuing combat sports. 

##### <u>Scope</u>

###### Functional Requirements:

Able to create accounts, reset password, add items to basket, make purchases, access and edit profile, access order history, logout. 

**Create Account**: Register with a valid email to create an account, that will gain access to being able to add items to the individual's basket/cart. 

**Shop**: Shop is accessible without having  to create to account to give viewer's an idea of what can be purchased and if the services provided suit their interest or needs before having to create an account. 

**Basket**: Items added to the basket will stay in the basket persistently. Adding over 5 items to the basket will result in a 10% discount from the total bill. 

**Payment**: Payment is powered by Stripe to protect user's payment information. Stripe will protect against invalid card details. Payment will not be allowed if the basket is empty or the transaction created does NOT have the status of 'PENDING'.

**Edit Profile**: A feature provided for users who might want to update essential details especially after purchase so that they can describe to the service provider a little more about themselves such as injuries or additional information. Additional information always contributes to improving overall results for the customers. 

**Order History**: Enables users who have made payment have a sense of reassurance that there is a record of their purchase and its current status. 

**Logout**: User can log out of their accounts for security reasons.

**Administrator Page**: Admin users can update edit existing shop items, add new shop items, edit user profiles, update individual transaction status. 

###### Content Requirements:

In order to load the functional components, database entities includes:
1) Each User's account information
2) Transaction Details,
3) Charge Details for each transaction that has been paid for
4) Invoice Items to record each item in each transaction and the quantity purchased.
5) 

##### <u>Structure</u>

Structure of the website follows a similar approach to a typical e-commerce website, where the navbar is located up the top. Shop items spaced out evenly. Profile, Basket and Payment pages are centralised on the page for easy reading and eventually easy selection and payment. 

Important and frequently accessed items such as the shop and basket are accessible directly visa icons while other features such as order history and password reset are found in a dropdown menu. 

State Changes such as invalid mobile numbers are signaled across the top to inform the user that an error has occured. At the same time, when information has been processed successfully, the user is either informed via those message tabs across the top or redirected to another page such as the 'thank you' page after payment has been processed. 

The  structure  defines  the  way  in  which  the  various  features  andfunctions of the site fit together. Just what those features and func-tions are constitutes the scopeof the site. Some sites that sell booksoffer a feature that enables users to save previously used addressesso they can be used again. The question of whether that feature—orany feature—is included on a site is a question of scope******

README: (markdown)
-Summary about what the project is about.  (be very neutral, third person perspective)
-How it works ( walk through on how to get started, needs to be intuitive)
-A live version can be found here
-Testing the features, use table with 3 columns: steps, expected results, pass/fail - can include a pdf file for reference if the testing is too long.
(test for happy case, unhappy cases, and fringe cases e.g quantity cant go negative, user types in very long characters. )
test case 1--> test if user can sign up for account, step 1. user type in the URL of website -- user sees landing page step 2 user clicks on the signup button -- user see a forms that asks for his details. 
step 3. user fills in the form with valid email, etc and press submit button. 
test case 2-->test if user will be prevented from signing up if he does not provide a valid email
-UI/UX: 5layers, scope, skeleton, strategy, structure, surface, include user stories, include wireframe and ER diagram in github as well.
-Technologies used 
-Features(stuff u want to brag about, these are the features and this is where they will come into action)
-Algorithms(only if u have special algorithms)
-Deployment: Condense the instructions for deplpying to heroku, talk about S3. 
-todos
-credits


add crispy forms instructions:
https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

set customised password reset forms:
https://wsvincent.com/django-user-authentication-tutorial-password-reset/

animate on scroll functionality
https://michalsnik.github.io/aos/

animate on click functionality
https://github.com/daneden/animate.css

Stripe branding 
https://stripe.com/en-sg/newsroom/brand-assets

how to show images from objects on django:
https://stackoverflow.com/questions/9498012/how-to-display-images-from-model-in-django

credit for user photo that auto uploads as profile picture for users
<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

instructions on how add filter by group on templates
https://stackoverflow.com/questions/4789021/in-django-how-do-i-check-if-a-user-is-in-a-certain-group

sending emails to admin personal email account
https://madradavid.com/sending-email-django-and-mailgun/



to-dos:


enterprise use - 10-50%-off discount code
email invoice in pdf both to enterprise and customer. 
about personal trainer page
add referral code functionality to admin page
email admin account when a purchase has been made
change debug to False!
edit profile, does not check for existing usernames and emails before changing
email account validation? 
Feedback email after I mark the transaction as 'delivered'
newsletters