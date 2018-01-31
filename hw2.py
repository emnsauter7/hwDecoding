# Homework 2 Template Code
#
# This file will query a randomly shifted text string from http://goo.gl/RssCBE.
# This string is loaded as a variable named scambledText and also saved to the file scrambledText.txt
# Your assignment is to programmatically determine the random shift value and then decode the text.
# Pass the decoded text to the variable named unscrambledText, and it will be save to a file unscrambledText.txt
# (It should be clear when you have decoded the text by the output you produce.)
#
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script

##################################################################
### HELPER CODE TO REQUEST RANDOM SCRAMBLED TEXT STRING FROM WEB
##################################################################
import requests
scrambledText=requests.get("http://goo.gl/RssCBE").text
f1=open('scrambledText.txt','wb')
f1.write(scrambledText.encode('utf8'))
f1.close()

##################################################################
### YOUR CODE TO DECODE AND CORRECT TEXT SHOULD GO BELOW HERE
##################################################################

# import anything else you might need here

email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS





unscrambledText='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

##################################################################
### HELPER CODE TO SAVE YOUR ANSWER
##################################################################
f2=open('unscrambledText.txt','wb')
f2.write(unscrambledText.encode('utf8'))
f2.close()
##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':2,'input':scrambledText,'output':unscrambledText}
