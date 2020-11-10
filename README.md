# instabot
This is an instagram bot that downloads images

this code uses reqiures selenium and chromedriver to be installed

chromedriver.exe should be in the path C:/webdrivers/chromedriver.exe

The secure file is used too store your facebook's user name and password.

FUNTIONS

login :- this function will use your facebook information placed in the secure file too log into instagram.
this is done because too view certain profiles a user might need to be authenticated.

takepic :- this funtion downloads the main picture on the first post after you have loged in.

takefirstpost:- this function downloads all the images that can be found int the first post on your feed after logging in.

downloaduser: this function is used too download all a user's post the parameter "user" should be the person's instagram username.This function can be called without logging in if the user's profle is public.

downloadloaded: This function takes the user's instagram username as it's parameter.it will download all images on the user's profile page that are loaded.

HELPER FUNCTIONS

downloadimgs: this function will download all images currently loaded on the display

getuser: this is a heaper funtion used too go to a user's profile page






