Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> 
>>> keyword = "Python"
>>> try:
	kv = {'wd':keyword}
	r = requests.get("http://www.baidu.com/s", params = kv)
	print(r.request.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print("Failed")

http://www.baidu.com/s?wd=Python
553255

>>> 
>>> 