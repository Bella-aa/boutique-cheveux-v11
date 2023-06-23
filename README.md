# **Boutique Cheveux Shop**

## **Website Intro**

Boutique Cheveux is an online ecommerce store where customers can purchase wig hair and hair care products to maintain their hair .

The live link of the website can be found > [HERE]()
 * deployed link > [clickhere](https://boutique-cheveux-6d3bebfaf3f2.herokuapp.com/)
 * link to github [clickhere](https://github.com/Bella-aa/boutique-cheveux-v11)

![Landing Page](https://github.com/Bella-aa/boutique-cheveux-v11/assets/103276740/65e3841b-7889-40b9-95b3-8aad111a6e83)

## Agile Methodology

* All user stories were entered as issues in the GitHub Kanban project. The live project board can be found on the repository's project tab or on the following link: [Bella's boutique](https://github.com/Bella-aa/boutique-cheveux-v11/issues)

![User Stories](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/0a6b2c88-c724-4eb3-9271-b7f229484f4b)

## UX Design

* *The UXD was created taking into consideration "The Five Planes"*

### Strategy plane

* Boutique Cheveux is designed as an ecommerce website where users can browse and purchase products in the shop and aswell as give thei opinion on cirtain products and find out more about the store/business

### Scope Plane

* The users will be able to create an account. After logging in, they will be able to browse and purchase antique furniture for delivery.

### Structure Plane

* Boutique Cheveux  website will have 6 main menus - All producs, Hair,Hair care, Subscribe, My Account and Shopping bag. On top of that, right in the middle a search box can be found to facilitate a easy browsing where users can type the specific product they are searching for.

### Skeleton Plane

* No wireframes were created for the creation of this website, as it was scrapped from the walkthrough project Boutique Ado.

### Surface Plane

* The chosen color scheme picked for the website is predominantly white and black. The main reason for this schema is the homepage background image that I chose.
* The colors of the navigation buttons were chosen to stand out from the main theme to get the attention of the user.
* The color contrast successfully passes using the [a11y](https://color.a11y.com/) contrast validator.

## SEO

* Keywords are used to associate website with Hair, haircare,, kinky hair, human hair, bonnets

## Business Model and Marketing Strategy

* The website is made for small businesses that promote Boutique Cheveux products and allows users to purchase items through the website directly from the owner of the website. This is a B2C - Business to Customer model, as it allows for direct communication between the owner of the items and customers.

### Facebook Page

* Social media is a great way to promote a business, in this case it is only a placeholder/mock-up page that I do not own.

![Facebook](https://github.com/Bella-aa/quiz-application/assets/103276740/a0861549-667a-4125-95c9-4358fd9845f6)

### Target Audience

* The Boutique Cheveux is for people of all ages and targets fans and collectors of artificial hair products.

## Data Modeling

* Database model relations between User, Product, Shopping Bag, Order, Reviews and  Newsletter.

* The different models compared to the walkthrough project are: Newsletter model were users are now able to subscribe to a newsletter so that they can recieve information about store offers and new stock. Review model were customers are able to write where they express their thoughts on a cirtain product . In this review model customers were also given the option function to rate the product to their liking .

![Data Model flow](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/aa4eccf7-4370-4f13-834e-6d6a76e46d91)

## Features

* The features represented by the website are :

### Landing Page

* This is the first page the user lands on when they open the website. The background image was chosen to attract the customers attenntion to the shop.

![main page](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/ff445e29-57f1-45a9-af34-a0ec8f020b5a)

### Navigation Bar

#### Desktop Navigation bar

  * Found on all widescreens the desktop navigation bar has the following features:
  * To the left side, the logo can be found.
  * To the right side the 3 main navigation links can be found: Subscribe, My Account, and Shopping bag.
  * Right in the middle, the search box can be found.
  * While a user is not logged in, another 2 links will be presented as a drop-down from My account: Register, and Login.
    * In Addition, while the user is logged in My Account navigation link dropdown menu will have the following links: My Profile, and Logout.
    * If the user is logged in as a superuser/website admin, My Account will have an additional link: Product Management coming up first.

![Desktop nav](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/56154177-40a1-423b-9bb1-bab9c7844696)

 ![admin](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/8835c79d-ec27-44c3-adad-6792d9ed25da) ![User](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/2796a790-3cd0-425e-9822-7c3ebbe66530)

* Below the main navigation row, another 3 drop-down links to navigate the list of products can be found in the middle of the row: All Products, Hair and Hair care
* All Products link will contain 4 sorting links to make browsing easier: By Price, By Rating, By Category, and All Products.

![All products](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/bdf44a4d-2ab1-4a25-8b03-f1a3ebcdc894)

* Hair  link will contain another 4 sorting links to facilitate browsing by category of the different types of hair available  and All hair  and the Hair care will also have similar links.

![Hair](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/2c4f31b8-8c03-4ffc-a132-db9c373394a4)  ![Hair care](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/46aaacca-c50b-4a59-a27d-eeabb09d2844)

#### Mobile Navigation bar

* Found on all medium and small screens the mobile navigation bar has the same features but with a different design.

![mobile view](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/00fdfb5b-a6d1-404b-99ae-7a4e4357c5ce)

### Authentication Pages

#### Sign Up

* On this page, you can register a new account by filling in the email address, username, and the password

![Sign up](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/24ee9c8c-016c-4e66-8447-88a6be97cdb5)

#### Sign In

* This is the sign-in/log-in page where users can authenticate their credentials to log in to the website or click forgot password in case they forget their password, in which case an email will be sent to with a link that will help them reset their password.

![Sign in](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/ebe08d58-0ef5-43c4-b0cf-0ad9a035eb55)

### Products Page

* Navigating to All Products page, you can find the list of the products available for sale, with options for sorting as it is observed here, sorted by category starting from 4 items in line starting on large screens and going down to a single item on the small screens and in addition a scroll back to rop button can be found to facilitate browsing. Clicking on any product picture, name or price will lead to a new page leading to the selected product.

![Products](https://github.com/Bella-aa/quiz-application/assets/103276740/ce3a0fcd-9a16-41a3-a5e3-0e739c7c1d11)

#### **Selected Product**

* This is the page of any selected individual product, options here are:
  * Product description
  * Edit and delete for admins.
  * Increase or decrease quantity, add to bag, and return to the products page by clicking keep shopping.

![Individual product](https://github.com/Bella-aa/quiz-application/assets/103276740/0bdeb324-4eac-42de-b26c-d9e9245fbb54)

### Reviews Pages

* Once a product is selected on the bottom, users can find the reviews with a button to a review, which will lead them to a form page where they can add a review and a rating. Site admins/staff members can edit or delete reviews in case of inappropriate language usage.

![Review](https://github.com/Bella-aa/quiz-application/assets/103276740/106e4534-102f-478d-9dd8-31dea8a94f64)


* Review update, for admins only.

![update review](https://github.com/Bella-aa/quiz-application/assets/103276740/930d2863-6275-45de-9504-89a59687d0aa)


* Review deletions, for admins only.

![Screenshot 2023-06-23 185341](https://github.com/Bella-aa/quiz-application/assets/103276740/875e0cee-2f3d-4b05-a66d-e3c2d93edc3c)


### Bag Page

* Product info, Price, Quantity, Subtotal, Bag total, Delivery price, and the Grand Total price. In addition, 2 buttons can be found Keep shopping to return back to products to facilitate browsing and Secure Checkout to move to the payment page, so the user can purchase the selected products.

![Screenshot 2023-06-23 185550](https://github.com/Bella-aa/quiz-application/assets/103276740/9684e6d8-0382-4d4a-8943-11ee6fe3735b)


### Checkout Page

* This is the checkout page, where the user can fill in their personal details, and card details to make a purchase, in addition, the order summary can be found on the right side. Also at the bottom, 2 buttons can be found, so the user can adjust their bag or complete the order once the details have been introduced.

![Checkout page](https://github.com/Bella-aa/quiz-application/assets/103276740/27b0500d-3491-49a4-b289-9e9430563c6c)


* After the user completed their order, they will be redirected to another page where they can view the confirmation details of their order. The user can press back to products to continue browsing.

![checkout sucess](https://github.com/Bella-aa/quiz-application/assets/103276740/47c3247a-e66f-4b1e-b85f-33b1e8c08f8f)


### Subscribe Page

* This is the subscribe page, where site users or visitors can fill in their email address to receive a newsletter about the website and new products and offers.

![subscribe](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/41704ea7-c070-4f61-b368-5505d1040b7a)

### Product Management

* On this page, leading down from the My Account drop-down link by clicking Product Management site admins/staff members can add new products for sale on the website.

![Screenshot 2023-06-18 105721](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/0c6479df-75b7-48db-905c-3eef56a3c370)

### My Profile

* On this page, leading down from the My Account drop-down link by clicking My Profile site users can update their personal details.

![Screenshot 2023-06-18 105903](https://github.com/Bella-aa/boutique-cheveux-v3/assets/103276740/4e09e792-cfaf-4f70-9c73-e8fc6c0a423c)

### Toasts

* Toasts are confirmation messages to the user's actions for a better experience on the website, so users can feel the impact of their actions on the website and to be assured that they have completed the action.

### Footer

* At the bottom of all pages the footer can be found serving social media links and copyright mark.

![footer image](https://github.com/Bella-aa/quiz-application/assets/103276740/3180ec1d-34a2-49ec-9ed8-419511a8f375)


## Technologies Used

* Python
  * The packages installed for the is project can be found in the **requirements.txt**
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* ElephantSQL, PostreSQL database
  * Used for the database during development and in deployment.
* HTML
  * HTML was the base language used to layout the skeleton of all templates.
* CSS
  * Custom CSS used to style the page and make the appearance look a little more unique.
* Javascript
  * I have used Javascript for Toasts and Stripe payments.
* Bootstrap
  * Used to style HTML, CSS. 
* Font awesome
  * All icons throughout the page.

## Deployment

The project was deployed onto heroku following all the steps outlined in the walkthrough migrating the project to a different data base.


## Testing

For this project manual testing was applied:

Constant use of "Run and Debug". This was the most used method of debugging:

* Add a breakpoint to the function currently in test, and check line by line if your variables behaves as intended.

Manual testing occurred regularly throughout local development, making use of statements that would print information to the console and use the Django debug pages.

All links redirects, and functionalities for purchasing products have been manually tested with success.

The website was tested on:

* Browsers: Firefox, Chrome,  and Microsoft Edge.
* Devices: Personal Samsung laptop, hp laaptop, Samsung A7 device, Iphone 12

### Fixed Bugs

hgjgckh

### Known Bugs

* The sorting products by category , price and rating is not working. I wish to revisit these errors and fix them so that users can be provided with the functionality for better user experience in the store.

## Credits

* Thanks to tutor support, they guided me through all the time I when I got stuck .

### General reference

* Besides the course's material I also used W3schools, youtube, Stack Overflow, and Django documentation for general or more in-depth reference for the other things I needed.

### Content and Media

* The content of the website was written by myself.
* The structure of the website was scrapped from the walktrough project Boutique Ado.
* Font linked from [Google Fonts](https://fonts.google.com/).
* All images were taken from the public domain with full royalty-free copyright.
































