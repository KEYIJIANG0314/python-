Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r = requests.get("https://item.jd.com/2967929.html")
>>> r.status_code
200
>>> r.encoding
'UTF-8'
>>> r.apparent_encoding
'ascii'
>>> r.text[:1000}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> r.text[:1000]
"<script>window.location.href='https://passport.jd.com/uc/login?ReturnUrl=http%3A%2F%2Fitem.jd.com%2F2967929.html'</script>"
>>> r = requests.get("https://item.jd.com/100011833542.html")
>>> r.status_code
200
>>> r.encoding
'UTF-8'
>>> r.text[:1000]
"<script>window.location.href='https://passport.jd.com/uc/login?ReturnUrl=http%3A%2F%2Fitem.jd.com%2F100011833542.html'</script>"
>>> r.encoding = 'gbk'
>>> r.text[:1000]
"<script>window.location.href='https://passport.jd.com/uc/login?ReturnUrl=http%3A%2F%2Fitem.jd.com%2F100011833542.html'</script>"
>>> url