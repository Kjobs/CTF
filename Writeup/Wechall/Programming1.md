Programming 1
--------

好久没有来wechall做题了，今天来逛了一下。做了了编程题。
```
When you visit this link you receive a message.
Submit the same message back to http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message
Your timelimit is 1.337 seconds
```
题目大概意思是说前往链接页面获取信息，在把信息作为post数据进入另一个页面。中间时间不超过1.337秒。想到最近学习的python selenium中的webdriver网页页面自动交互，于是进行了一番尝试。

下面时源代码：
```python
#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

def main():
	driver = webdriver.Chrome()
	driver.get("http://www.wechall.net/")

	#实现wechall的登录
	username_input = driver.find_element_by_xpath("//input[@name='username']")
	username_input.send_keys("user*****")
	password_input = driver.find_element_by_xpath("//input[@name='password']")
	password_input.send_keys("pass*****")
	driver.find_element_by_xpath("//input[@name='bind_ip']").click()
	driver.find_element_by_xpath("//input[@name='login']").click()
	driver.forward()

	#转到challenge页面
	driver.find_element_by_xpath("/html/body/div[1]/nav/ul/li[7]/a").click()
	driver.forward()

	#转到Programming1页面
	p1 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/table/tbody/tr[9]/td[2]/a[1]")
	p1.click()
	driver.forward()

	#跳转到链接页面获取文本信息
	link = driver.find_element_by_link_text("this link")
	link.click()
	driver.forward()
	#获取信息
	text = driver.find_element_by_xpath("/html/body").text
	print text

	#跳转到目的页面
	base_url = "http://www.wechall.net/challenge/training/programming1/index.php?answer="
	url = base_url+text
	driver.get(url)
	driver.forward()

	sleep(10)

if __name__ == '__main__':
	main()
```

中间一些Xpath路径是直接用火狐插件复制的，以后尽量还是写一些简便的吧。
