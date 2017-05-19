#!/usr/bin/python3

import cgi

#import cgitb
#cgitb.enable()

import requests 
from requests.auth import HTTPBasicAuth

import json


print ("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers


form = cgi.FieldStorage() 

mail_to = form.getvalue('to')
mail_subject = form.getvalue('subject')
mail_body = form.getvalue('body')
mail_send_key = form.getvalue('key')
captcha_key = form.getvalue('g-recaptcha-response')


#captcha
cap_url = 'https://www.google.com/recaptcha/api/siteverify'
cap_postdata = {'secret': '6Lc-CyEUAAAAAHNQMGF52XvXD8yb48L4iodqSOat', 'response': captcha_key}
captcha_request = requests.post(cap_url, params=cap_postdata)

if captcha_request.json()['success'] == True and mail_send_key == 'maauer':
	
	# send mail
	mail_from = 'maauer mail script <maauer-public-mail-script@public.untrust.output.maauer.com>'
	url = 'https://api.mailgun.net/v3/output.maauer.com/messages'
	postdata = {'from': mail_from, 'to': mail_to, 'subject': mail_subject, 'text': mail_body, 'html': mail_body} 
	mail = requests.post(url, params=postdata, auth=HTTPBasicAuth('api', 'key-0ab82a130ef38a16655849f0fb11237d'))

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

