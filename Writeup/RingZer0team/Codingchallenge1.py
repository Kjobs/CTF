```python
#-*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import hashlib
import re

def hash_info(message):
	return hashlib.sha512(message).hexdigest()

def message_match(message):
	#替换空白字符，便于后续处理
	strinfo = re.compile(r'[\s]*')
	message = strinfo.sub('',message)
	#提取message信息
	pattern = re.compile(r'([\-]*)(\w+)([\-]*)(\w*)([\-]*)(\w+)([\-]*)')
	final_message = re.match(pattern,message)
	return final_message.group(4)

def main():
	driver = webdriver.Chrome()
	driver.get("https://ringzer0team.com/")

	#进入网站登录页面
	log_in = driver.find_element_by_xpath("/html/body/nav/div/div[2]/div/a")
	log_in.click()
	driver.forward()

	#填写登录信息进行用户登陆
	username_input = driver.find_element_by_xpath("//input[@name='username']")
	username_input.send_keys("user***")
	password_input = driver.find_element_by_xpath("//input[@name='password']")
	password_input.send_keys("pass***")
	driver.find_element_by_xpath("//input[@class='form-control btn btn-success']").click()
	driver.forward()

	#点击进入challenge13
	driver.get("https://ringzer0team.com/challenges/13")
	driver.forward()

	#获取message信息并利用hash_info函数进行加密
	message = driver.find_element_by_xpath("//div[@class='message']").text
	message = message_match(message)
	hash_message = hash_info(message)

	#发送信息给目标网址
	url = "https://ringzer0team.com/challenges/13/"
	bt_url = url+str(hash_message)
	driver.get(bt_url)
	driver.forward()

	sleep(10)

if __name__ == '__main__':
	main()
	```
