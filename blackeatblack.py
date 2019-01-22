import urllib
import urllib2
import random

requrl = "http://sedujiko.cf/verifyAlim.php"

domain_dic = ['.cn','.com','.net','.top','.xyz','.vip','.edu','.tt','.ooo','.xxx','.org']

headers = [{"Content-type": "application/x-www-form-urlencoded",
			'Accept-Language':'zh-CN,zh;q=0.8',
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Connection": "close"},
		   {"Content-type": "application/x-www-form-urlencoded",
			'Accept-Language':'zh-CN,zh;q=0.8',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Connection':'keep-alive'},
		   {"Content-type": "application/x-www-form-urlencoded",
			'Accept-Language':'zh-CN,zh;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
			'Accept': 'text/html, */*; q=0.8',
			'Connection':'keep-alive'},
		   {"Content-type": "application/x-www-form-urlencoded",
		    'Accept-Language':'zh-CN,zh;q=0.8',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
			'Accept': 'text/html, */*; q=0.8',
			'Connection':'keep-alive'}]

while True: 

	password_length = random.randint(12,20)
	password = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()",password_length))
	username_length = random.randint(1,20)
	username = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz",username_length))
	domain_length = random.randint(3,20)
	domain = ''.join(random.sample("abcdefghijklmnopqrstuvwxyz",domain_length))
	domain_index = random.randint(0,10)
	email = username + "@" + domain + domain_dic[domain_index]
	header_index = random.randint(0,3)
	 
	test_data = {'Email': 'sb@sb.com', 'Password': 'nmsl'}
	test_data['Email'] = email
	test_data['Password'] = password
	test_data_urlencode = urllib.urlencode(test_data)

	req = urllib2.Request(url=requrl, headers = headers[header_index], data=test_data_urlencode)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print(email)
	print(password)
	print(header_index)
	print(req)
	print(response)
	print(the_page[:100])
