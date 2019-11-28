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

### <u>Strategy</u>





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



to-dos:


enterprise use - 10-50%-off discount code
email invoice in pdf both to enterprise and customer. 
about personal trainer page
add referral code functionality to admin page
add 'adding and deleting shop item' feature to admin page
change debug to False!

unable to upload images! possibly because of models error! (upload to?) - admin page edit shop item and adding new stock
unable to change referral code active to non-active
stock levels not updating after purchase 
invoice item not recording transaction items after purchase