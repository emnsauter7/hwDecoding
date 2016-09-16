#Run this script at the end when you are ready to submit your homework to the autograder.

import hw2solutions as hw2  # imports your hw2 module
import requests

submissionFile=open('hw2.py','r')
postData=hw2.yourSubmission()


tokenFile=open('token','a+')
token=tokenFile.read();

if len(token)==0: 
	tokenResponse=requests.post("https://script.google.com/macros/s/AKfycbzcEo7CyYd4CIN_A_rw6S_LgJmvBxN6yB57vzreuVzvpmERsIf-/exec",data={'requestingToken':1,'email':postData["email"]});
	token=tokenResponse.text;
	tokenFile.write(token)

postData["token"]=token
postData["submission"]=submissionFile.read()
subResponse=requests.post("https://script.google.com/macros/s/AKfycbzcEo7CyYd4CIN_A_rw6S_LgJmvBxN6yB57vzreuVzvpmERsIf-/exec",data=postData)
responseFile=open('submissionResponse.txt','w+')
responseFile.write(subResponse.text.encode('utf8'))
print subResponse.text
