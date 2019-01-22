# blackeatblack

```
import urllib
import urllib2
import random

requrl = "http://sedujiko.cf/verifyAlim.php"

domain_dic = ['.cn','.com','.net','.top','.xyz','.vip','.edu','.tt','.ooo','.xxx','.org']

while True: 

	password_length = random.randint(12,20)
	password = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()",password_length))
	username_length = random.randint(1,20)
	username = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz",username_length))
	domain_length = random.randint(3,20)
	domain = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz",domain_length))
	domain_index = random.randint(0,10)
	email = username + "@" + domain + domain_dic[domain_index]
	 
	test_data = {'Email': 'sb@sb.com', 'Password': 'nmsl'}
	test_data['Email'] = email
	test_data['Password'] = password
	test_data_urlencode = urllib.urlencode(test_data)

	req = urllib2.Request(url=requrl, data=test_data_urlencode)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print(email)
	print(password)
	print(req)
	print(response)
	print(the_page[:100])
```

Create a python script to post fake data to phishing website page, yeah, it is boring! 😆
