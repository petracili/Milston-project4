<h1 aligin="center">The Croatian Wine</h1>

Code Institute Diploma in Full-Stack Software Development Project 4

##### <u>Project name:</u>The Croatian Wine

You can find the live site [here](https://myston-project-4.herokuapp.com/)

---
---
# Contents
+ [User Experience](#user-experience)
  + [User Stories](#user-stories)
  + [Design](#design)
    + [Overall Feel](#overall-feel)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
  + [Wireframes and Initial Design](#wireframes-and-initial-design)
    + [Wireframes](#wireframes)
    + [Design Mock Up](#design-mock-up)
+ [Features](#features)
  + [Current Features](#current-features)
  + [Possible Future Features](#possible-future-features)
  + [Defensive Design Features](#defensive-design-features)
+ [Database](#database)
+ [Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Frameworks and Libraries](#frameworks-and-libraries)
  + [All Others](#all-others)
+ [Testing](#testing)
+ [Deployment](#deployment)
  + [Heroku Deployment](#heroku-deployment)
  + [Set up AWS](#set-up-aws)
  + [Set up Emails](#set-up-emails)
  + [Forking the Repository](#forking-the-repository)
  + [Making a Local Clone](#making-a-local-clone)
+ [Credits](#credits)
  + [Content](#content)
  + [Media](#media)
  + [Acknowledgements](#acknowledgements)

---
---
# User Experience
## User Stories

### As an unregistered, I want to :

+ be able to browse through all products available.
+ have the ability browse through the wine promoted on the site.
+ have the ability to contact the wine promoted on the site.
+ have generic questions answered without having to contact the store owner/admin.
+ be able to view my bag and any items I currently have awaiting payment in my bag.
+ be able to add, edit quantity and remove items from my bag.
+ be able to purchase from the site without having to register for an account.
+ have the ability to register to the site if I choose to.

### As a registered user, I want to:

+ have the ability to log in to the site with  my details.
+ have a record of any purchases that I have made in the past and view them in detail.
+ be able to update my shipping information.
+ be able to update my shipping information from the checkout page. 

### As the site administrator, I want to:

+ be able to log in to an admin panel.
+ be able to add, update or remove products, wine without vistiting the admin panel.
+ receive email notifications when a user submits through the contact page.

---
---
# User Experience
## User Stories

### As an unregistered, I want to :

+ be able to browse through all products available.
+ have the ability browse through the wine promoted on the site.
+ have the ability to contact the wine promoted on the site.
+ have generic questions answered without having to contact the store owner/admin.
+ be able to view my bag and any items I currently have awaiting payment in my bag.
+ be able to add, edit quantity and remove items from my bag.
+ be able to purchase from the site without having to register for an account.
+ have the ability to register to the site if I choose to.

### As a registered user, I want to:

+ have the ability to log in to the site with  my details.
+ have a record of any purchases that I have made in the past and view them in detail.
+ be able to update my shipping information.
+ be able to update my shipping information from the checkout page. 

### As the site administrator, I want to:

+ be able to log in to an admin panel.
+ be able to add, update or remove products wine without vistiting the admin panel.
+ receive email notifications when a user submits through the contact page.


## Design
### Overall Feel

For this page I wanted a modern industrial look in a combination of white and gray. to make the page look more elegant

### Colour Scheme

While white is the main colour for the site and will be itilized as much as possible, I chose gray colours that I thought would not be overwhelming and add an elegance to it. 

### Typography

I chose the [Nunito](https://fonts.google.com/specimen/Nunito?query=Nunito) font for the all site.

### Imagery

The imagery throughout the site will be primarily dictated by the products for sale.

However, I chose photos of wine that are very popular in Croatia and thus tried to introduce people to Croatian wine production.

Due to too large file all images are processed in [TinyPNG] (https://tinypng.com/).



## Wireframes and Initial Design

As the project progressed, some element placement was tweaked and updated. However, I think that the layout changes were not so drastic that they warrented new wireframes to be designed and I also had limited time for project development .You can find it [here](https://github.com/petracili/Milston-project4/tree/main/wireframes). 

---
---

---
---

# Features
## Current Features
### **Navigation menu displayed across all pages**

The navigation menu will help the user move easily across all pages.

The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

| Nav Link              |Not logged in  |Logged in as user|Logged in as admin
|:-------------         |:------------- |:----------------|:------------- |
|Logo(back to home)     |&#9989;        |&#9989;          |&#9989;
|Product Management     |&#10060;       |&#10060;         |&#9989;
|Wine Management      |&#10060;       |&#10060;         |&#9989;
|My Profile             |&#10060;       |&#9989;          |&#9989;
|Sign Out               |&#10060;       |&#9989;          |&#9989;
|Register               |&#9989;        |&#10060;         |&#10060;
|Sign In                |&#9989;        |&#10060;         |&#10060;
|All Products           |&#9989;        |&#9989;          |&#9989;
|Prints                 |&#9989;        |&#9989;          |&#9989;

### **User registration not required**

It was important that the user was given the option to purchase from the store without having to register for an account. It's a personal pet peeve of mine to have to make accounts on online stores when I'm not guaranteed to go back again.

### **User profile creation**

A user has an option to create an account if they want to. 
Registration process:

+ Username
   + A user can choose a username as long as it hasn't already been taken
   + The user will receive an error notification immediately if their username has already been taken

+ Email address
   + A user needs to sign up using an email address
   + The email has to be inputted twice to avoid typo issues
   + This triggers an automatic email to be sent to the user to confirm the email address as correct and set up the account. 

+ Password
   + The password has to be inputted twice to avoid typo issues

With a user profile: 
+ order history is saved & displayed in their profile.
+ Save default delivery information to their profile from the checkout page.
+ Update default delivery information to their profile from their profile page.

---

# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](). 

---
---

# Deployment

## Heroku Deployment
This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ Create your Procfile and insert the following code: ```web: gunicorn croatian_wine.wsgi``` and make sure there is no additional blank line after it. 
+ Push these files to your repository.

### Creating Heroku App
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropriate region based on your location
+ Click 'Create App'

### Connecting to GitHub
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this.

### Environment Variables
+ Click the 'Settings' tab towards the top of the page
+ Locate the 'Config Vars' and click 'Reveal Config Vars'
+ The following variables all need to be added:

|Variable name         |Value/where to find value                                |
| ---------------------|---------------------------------------------------------|
|AWS_ACCESS_KEY_ID     |AWS CSV file(instuctions below)                          |
|AWS_SECRET_ACCESS_KEY |AWS CSV file(instuctions below)                          |
|DATABASE_URL          |Postgres generated (instructions below)                  |
|EMAIL_HOST_PASS       |Password from email client                               |
|EMAIL_HOST_USER       |Site's email address                                     |
|SECRET_KEY            |Random key generated online                              |
|STRIPE_PUBLIC_KEY     |Stripe Dashboard > Developers tab > API Keys > Publishable key |
|STRIPE_SECRET_KEY     |Stripe Dashboard > Developers tab > API Keys > Secret key |
|STRIPE_WH_SECRET      |Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
|USE_AWS               |True (when AWS set up - instructions below)              |

### Heroku Postgres Database
+ Go to the resources tab in Heroku.
+ In the Add-ons search bar look for Heroku Postgres & select it.
+ Choose the Hobby Dev-Free option in plans.
+ Click submit order form.
+ Go back to the build environment and install 2 more requirements:
  + ```pip3 install dj_databse_url```
  + ```pip3 install psycopg2-binary```
  make sure to add these to the requirements file using ```pip3 freeze > requirements.txt``` 

## Set up AWS

### AWS S3 Bucket
+ From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
+ Click 'Create a new bucket', give it a name(associated with the Heroku app name), and choose the region closest to you.
+ Make sure that 'Block all public access' is **unchecked**(you may need to confirm that public access will be given).
+ Ignore any other settings that you are asked to change and click 'Create bucket'.
+ Open the created bucket, go to the 'Properties' tab and turn on static website hosting(fill in index.html and error.html as defaults) and click save.
+ Open the 'Permissions' tab, locate the CORS configuration section and add the following code:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
+ In the 'Bucket Policy' section click 'Edit' > 'Policy Generator'.
+ Choose 'S3 Bucket Policy' from the 'Select Type of Policy' dropdown.
+ In 'Step 2: Add Statements', add the following settings:
  + Effect: **Allow**
  + Principal: **" * "** (no quotation marks)
  + Actions: **GetObject**
  + ARN: **Bucket ARN** (get from S3 Bucket page)
+ Click 'Add Statement'.
+ Click 'Generate Policy'.
+ Copy the policy from the popup that appears
+ Paste the generated policy into the Permissions > Bucket Policy area.
+ Add '/*' at the end of the 'Resource' key, and save.
+ Go to the 'Access Control List' section, and select 'List' next to 'Everyone'.

### AWS IAM (Identity and Access Management)
+ From the 'Services' tab on the AWS Management Console, search IAM and select it.
+ Go to 'User Groups' > 'Create New Group' > choose a name(associated with the S3 Bucket name) and click 'Create'.
+ Go to 'Policies' > 'Create New Policy' > 'JSON' > 'Import Managed Policy' > search 'S3' > select 'AmazonS3FullAccess' > Click 'Import'.
+ Get the bucket ARN from 'S3 Permissions'
+ Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "{PASTED ARN}",
    "{PASTED ARN}/*"
]
```

+ Click 'Next' > 'Review' > provide a name and description(associated with the S3 Bucket name), and click 'Create Policy'.
+ Go to 'User Groups'> Open the created group > 'Permissions' > 'Add Permissions' > 'Attach Policies' > search for the policy you created and click 'Add Permissions'.
+ Go to 'Users' > 'Add Users' > create a name and select 'Programmatic access' for the 'Access Type' option.
+ Click 'Next' and select the group you created.
+ Keep clicking 'Next' until you reach the 'Create user' button and click that. 
+ Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables.
+ **This will be the only time that you will be able to access and download this file. If you don't download it, you'll have to start the AWS process again**

## Set up Emails

**I used Gmail for the email account. Others can be used but will need a few changes**

+ Go to settings.py and change the DEFAULT_FROM_EMAIL to your chosen email address.
+ If you want to set up a new Gmail account for the site, this is the time to do so.
+ Go to the Gmail account and open the 'Settings' tab.
+ Go to 'Accounts and Imports' > 'Other Google Account Settings'.
+ Go to the 'Security' tab and open 'Signing in to Google'.

+ Click on '2-step Verification', click 'Get Started' and turn on 2-step verification following their instructions.
+ Go to 'Security' > 'Signing in to Google' > 'App Passwords'.
+ (You may have to input your account password again) Set 'App' to 'Mail', 'Device' to Other, and name it Django.
+ The passcode that appears will be used in your Heroku variables.

## Deploy
+ In Heroku, once all the variables are in place, locate 'Manual Deploy' > choose the master branch and click 'Deploy Branch'.
+ Once the app is built (it may take a few minutes), click 'Open App' from the top of the page.
+ Go back to the 'Deploy' tab and you can now click 'Enable Automatic Deployment'. Changes automatically deploy when you make a git push.

## Forking the Repository
+ Log in to GitHub and locate the GitHub Repository.
+ At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
+ You will have a copy of the original repository in your GitHub account.
+ You will now be able to make changes to the new version and keep the original safe. 

## Making a Local Clone
+ Log into GitHub.
+ Locate the repository.
+ Click the 'Code' dropdown above the file list.
+ Copy the URL for the repository.
+ Open Git Bash on your device.
+ Change the current working directory to the location where you want the cloned directory.
+ Type ```git clone``` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  + ```$ git clone ```
+ Press Enter to create your local clone.