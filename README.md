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

Manual Testing was conducted and the documentation can be found [on github](https://github.com/jaymanmt/PMT) in a pdf file.


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

**Payment**: Payment is powered by Stripe to protect user's payment information. Stripe will protect against invalid card details. Payment will not be allowed if the basket is empty or the transaction created does NOT have the status of 'PENDING'. 10% discount applied if 5 packages and above purchased. Additional 10% off with use of discount code. 

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
5) Referral Codes to store unique referral codes.
6) Basket entity to store individual users' cart items. 
7) Item to store  shop items and their individual details.
8) Categories to better organise types of Shop Items

##### <u>Structure</u>

Important and frequently accessed items such as the shop and basket are accessible directly visa icons while other features such as order history and password reset are found in a dropdown menu. 

State Changes such as invalid mobile numbers are signaled across the top to inform the user that an error has occured. At the same time, when information has been processed successfully, the user is either informed via those message tabs across the top or redirected to another page such as the 'thank you' page after payment has been processed. 

##### <u>Skeleton</u>

Struture of the website follows a similar approach to a typical e-commerce website, where the navbar is located up the top. Shop items spaced out evenly. Profile, Basket and Payment pages are centralised on the page for easy reading and eventually easy selection and payment. 

A wireframe for structure was not used for this website as the structure of the webpage follows a simple e-Commerce layout. 

##### <u>Surface</u>

White-ish background with darker undertones to represent a form of elegancy through out website. Stuck with 5 color themes through out, red, yellow, black and white.
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

- Add more discount codes
- ability to send newsletters via admin page

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