#!/usr/bin/python3

import cgi

#import cgitb
#cgitb.enable()

import requests 
from requests.auth import HTTPBasicAuth


print ("Content-Type: text/html")
print()


#get vars from apache
form = cgi.FieldStorage() 

mail_to = form.getvalue('to')
mail_subject = form.getvalue('subject')
mail_body = form.getvalue('body')
mail_send_key = form.getvalue('key')
captcha_key = form.getvalue('g-recaptcha-response')


#captcha
captcha_url = 'https://www.google.com/recaptcha/api/siteverify'
captcha_postdata = {'secret': 'YOUR reCAPTCHA SECRET', 'response': captcha_key}
captcha_request = requests.post(captcha_url, params=captcha_postdata)

if captcha_request.json()['success'] == True and mail_send_key == 'CUSTOM KEY':
	
	# send mail
	mail_from = 'mail script <YOUR "FROM" ADDRESS>'
	url = 'https://api.mailgun.net/v3/YOUR-MAILGUN-DOMAIN/messages'
	postdata = {'from': mail_from, 'to': mail_to, 'subject': mail_subject, 'text': mail_body, 'html': mail_body} 
	mail = requests.post(url, params=postdata, auth=HTTPBasicAuth('api', 'YOUR MAILGUN API KEY'))

elif captcha_request.json()['success'] != True:
		print ('ERROR - mail not sent - CAPTCHA incorrect <br><br>')

else:
	print ('ERROR - mail not sent <br><br>')

# html-formatted  output
print ('<style> body {font-size:20px;} </style>')
print ('to: ' + mail_to)
print ('<br>')
print ('from: ' + mail_from)
print ('<br>')
print ('subject: ' + mail_subject)
print ('<br>')
print ('body: ' + mail_body)

print('<br><br>')
print (mail.json()['message'])

