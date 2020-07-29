Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> path = "C:/abc.jpg"
>>> url = "https://eunjiwonupdates.files.wordpress.com/2013/08/eun-ji-won-tumblr.jpg"
>>> r = requests.get(url)
>>> r.status_code
200
>>> with open(path, 'wb') as f:
	f.write(r.content)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    with open(path, 'wb') as f:
PermissionError: [Errno 13] Permission denied: 'C:/abc.jpg'
>>> path = "admin:/abc.jpg"
>>> with open(path, 'wb') as f:
	f.write(r.content)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    with open(path, 'wb') as f:
OSError: [Errno 22] Invalid argument: 'admin:/abc.jpg'
>>> path = "C:/abc.jpg"
>>> url = "https://eunjiwonupdates.files.wordpress.com/2013/08/eun-ji-won-tumblr.jpg"
>>> r = requests.get(url)
>>> r.status_code
200
>>> with open(path, 'wb') as f:
	f.write(r.content)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    with open(path, 'wb') as f:
OSError: [Errno 22] Invalid argument: 'C:/abc.jpg'
>>> path = "C:\Users\admin\Desktop\photos"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "C:/Users/admin/Desktop"
>>> path = "C:/Users/admin/Desktop/abc.jpg"
>>> url = "https://eunjiwonupdates.files.wordpress.com/2013/08/eun-ji-won-tumblr.jpg"
>>> r = requests.get(url)
>>> r.status_code
200
>>>  with open(path, 'wb') as f:
	f.write(r.content)
	
SyntaxError: unexpected indent
>>> with open(path, 'wb') as f:
	f.write(r.content)

396065
>>> f.close
<built-in method close of _io.BufferedWriter object at 0x0000016A820AA9E0>
>>> f.close()
>>> 
>>> 
>>> import requests
>>> import os
>>> url = "https://eunjiwonupdates.files.wordpress.com/2014/05/img.png"
>>> root = "C://Users//admin//Desktop//"
>>> path = root + url.split('/')[-1]
>>> try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("successfully downloaded")
	else:
		print("already exists")
except:
	print("failed")

498108
successfully downloaded


>>> 