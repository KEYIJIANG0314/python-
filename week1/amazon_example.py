Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r = requests.get("https://www.amazon.com/gp/product/B0027CTFDM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1")
>>> r.status_code
503
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = r.apparent_encoding
>>> r.text
'<!--\n        To discuss automated access to Amazon data please contact api-services-support@amazon.com.\n        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com/ref=rm_5_sv, or our Product Advertising API at https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html/ref=rm_5_ac for advertising use cases.\n-->\n<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <meta http-equiv="x-ua-compatible" content="ie=edge">\n  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n  <title>Sorry! Something went wrong!</title>\n  <style>\n  html, body {\n    padding: 0;\n    margin: 0\n  }\n\n  img {\n    border: 0\n  }\n\n  #a {\n    background: #232f3e;\n    padding: 11px 11px 11px 192px\n  }\n\n  #b {\n    position: absolute;\n    left: 22px;\n    top: 12px\n  }\n\n  #c {\n    position: relative;\n    max-width: 800px;\n    padding: 0 40px 0 0\n  }\n\n  #e, #f {\n    height: 35px;\n    border: 0;\n    font-size: 1em\n  }\n\n  #e {\n    width: 100%;\n    margin: 0;\n    padding: 0 10px;\n    border-radius: 4px 0 0 4px\n  }\n\n  #f {\n    cursor: pointer;\n    background: #febd69;\n    font-weight: bold;\n    border-radius: 0 4px 4px 0;\n    -webkit-appearance: none;\n    position: absolute;\n    top: 0;\n    right: 0;\n    padding: 0 12px\n  }\n\n  @media (max-width: 500px) {\n    #a {\n      padding: 55px 10px 10px\n    }\n\n    #b {\n      left: 6px\n    }\n  }\n\n  #g {\n    text-align: center;\n    margin: 30px 0\n  }\n\n  #g img {\n    max-width: 90%\n  }\n\n  #d {\n    display: none\n  }\n\n  #d[src] {\n    display: inline\n  }\n  </style>\n</head>\n<body>\n    <a href="/ref=cs_503_logo"><img id="b" src="https://images-na.ssl-images-amazon.com/images/G/01/error/logo._TTD_.png" alt="Amazon.com"></a>\n    <form id="a" accept-charset="utf-8" action="/s" method="GET" role="search">\n        <div id="c">\n            <input id="e" name="field-keywords" placeholder="Search">\n            <input name="ref" type="hidden" value="cs_503_search">\n            <input id="f" type="submit" value="Go">\n        </div>\n    </form>\n<div id="g">\n  <div><a href="/ref=cs_503_link"><img src="https://images-na.ssl-images-amazon.com/images/G/01/error/500_503.png"\n                                        alt="Sorry! Something went wrong on our end. Please go back and try again or go to Amazon\'s home page."></a>\n  </div>\n  <a href="/dogsofamazon/ref=cs_503_d" target="_blank" rel="noopener noreferrer"><img id="d" alt="Dogs of Amazon"></a>\n  <script>document.getElementById("d").src = "https://images-na.ssl-images-amazon.com/images/G/01/error/" + (Math.floor(Math.random() * 43) + 1) + "._TTD_.jpg";</script>\n</div>\n</body>\n</html>\n'
>>> r.apparent_encoding
'ascii'
>>> r.requests.headers
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    r.requests.headers
AttributeError: 'Response' object has no attribute 'requests'
>>> r.request.headers
{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> kv = {'user-agent':'Chrome/84.0'}
>>> url = "https://www.amazon.com/gp/product/B0027CTFDM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1"
>>> r = requests.get(url, headers = kv)
>>> r.status_code
503
>>> kv = {'user-agent':'Chrome/84.0'}
>>> url = "https://www.amazon.com/gp/product/B0027CTFDM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1"
>>> r = requests.get(url, headers = kv)
>>> r.status_code
SyntaxError: multiple statements found while compiling a single statement
>>> kv = {'user-agent':'Mozilla/5.0'}
>>> url = "https://www.amazon.com/gp/product/B0027CTFDM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1"
>>> r = requests.get(url, headers = kv)
>>> r.status_code
200
>>> r.request.headers
{'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> r.text[:1000]
'<!DOCTYPE html>\n<!--[if lt IE 7]> <html lang="en-us" class="a-no-js a-lt-ie9 a-lt-ie8 a-lt-ie7"> <![endif]-->\n<!--[if IE 7]>    <html lang="en-us" class="a-no-js a-lt-ie9 a-lt-ie8"> <![endif]-->\n<!--[if IE 8]>    <html lang="en-us" class="a-no-js a-lt-ie9"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class="a-no-js" lang="en-us"><!--<![endif]--><head>\n<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n<meta charset="utf-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n<title dir="ltr">Robot Check</title>\n<meta name="viewport" content="width=device-width">\n<link rel="stylesheet" href="https://images-na.ssl-images-amazon.com/images/G/01/AUIClients/AmazonUI-3c913031596ca78a3768f4e934b1cc02ce238101.secure.min._V1_.css">\n<script>\n\nif (true === true) {\n    var ue_t0 = (+ new Date()),\n        ue_csm = window,\n        ue = { t0: ue_t0, d: function() { return (+new Date() - ue_t0); } },\n        ue_furl = "fls-na.amazon.com",\n        ue_mid = "ATVPDKIKX0DER",\n   '
>>> import requests
>>> url = "https://www.amazon.com/gp/product/B0027CTFDM/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1"
>>> try:
	kv = {'user-agent':'mozilla/5.0}
	      
SyntaxError: EOL while scanning string literal
>>> try:
	kv = {'user-agent':'mozilla/5.0'}
	r = requests.get(url, headers=kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
	except:
		
SyntaxError: invalid syntax
>>> try:
	kv = {'user-agent':'mozilla/5.0'}
	r = requests.get(url, headers=kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
    except:
	    
SyntaxError: unindent does not match any outer indentation level
>>> try:
	kv = {'user-agent':'mozilla/5.0'}
	r = requests.get(url, headers=kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
... except:
	
SyntaxError: invalid syntax
>>> try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("error")

    
     ue_sid = (document.cookie.match(/session-id=([0-9-]+)/) || [])[1],
        ue_sn = "opfcaptcha.amazon.com",
        ue_id = '16264NQH9JV26M2M72DF';
}
</script>
</head>
<body>

<!--
        To discuss automated access to Amazon data please contact api-services-support@amazon.com.
        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com/ref=rm_c_sv, or our Product Advertising API at https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html/ref=rm_c_ac for advertising use cases.
-->

<!--
Correios.DoNotSend
-->

<div class="a-container a-padding-double-large" style="min-width:350px;padding:44px 0 !important">

    <div class="a-row a-spacing-double-large" style="width: 350px; margin: 0 auto">

        <div class="a-row a-spacing-medium a-text-center"><i class="a-icon a-logo"></i></div>

        <div class="a-box a-alert a-alert-info a-spacing-base">
            <div class="a-box-inner">
                <i
>>> 