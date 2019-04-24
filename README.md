# HackInOS-File-Upload-Finder
Just a place to keep a neat piece of code I made in order to assist in rooting the HackInOS machine on Vulnhub.

## What is this?
In the CTF vulnhub machine known as "HackInOS," at some point you may come across a place where you can upload files. In this case, I used this to upload a PHP reverse shell onto the VM's web server. Upon inspection of html source code you are able to find a link to a PHP file responsible for uploading the files to the web server. Long story short yada yada, I analyzed the code and found out where the uploaded files were being stored. (Long story short) The files were being stored based on hash combinations of the filename and a number between 1-100. I then wrote this script to brute force the url of the uploaded php reverse shell file. 

## Why am I uploading this?
Mainly just as a place to keep it for future reference, but also in hopes that someone else interested in CTF, or HTTP requests in python, or hashing in python, or really just anyone who is interested in this at all may find it. 

### Please let me know if you find this code interesting, useful, or if you learned something in any way. It might make my day!
