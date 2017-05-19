This is a python cgi script designed to run under apache.

Requirements:
- Python 3 (2 will probably work but I don't actually know)
- [Apache webserver](https://httpd.apache.org/)
- [Python cgi](https://docs.python.org/3/library/cgi.html)
- [Python Requests](http://docs.python-requests.org)
- cgitb (optional - for debugging)
- [Mailgun account](https://mailgun.com)
- [reCaptcha](https://www.google.com/recaptcha/intro/index.html)

An example can be found [here](https://maauer.com/projects/mailgun.html). The key is "maauer". the key is used to prevent spamming from random people (as it can be changed easily) and the captcha is used to protect against bots. 