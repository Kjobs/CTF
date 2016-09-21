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
	pattern = re.compile(r'([\-]*)(\w+)([\-]*)(\d*)([\-]*)(\w+)([\-]*)')
	final_message = re.match(pattern,message)
	return final_message.group(4)

def binary_to_str(message):
	#将得到的二进制信息转换为字符串
	decimal_list = []
	str = ""
	for i in range(0,len(message),8):
		num = int(message[i:i+8],2)
		decimal_list.append(num)
	for j in decimal_list:
		c = chr(j)
		str = str+c
	return str

def webdriver_login():
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

	#点击进入challenge14
	driver.get("https://ringzer0team.com/challenges/14")
	driver.forward()

	#获取message信息并利用hash_info函数进行加密
	message = driver.find_element_by_xpath("//div[@class='message']").text
	#获取二进制数据
	message_bin = message_match(message)
	#二进制转换为字符
	message_str = binary_to_str(message_bin)
	#进行SHA512加密
	hash_message = hash_info(message_str)

	#发送信息给目标网址
	url = "https://ringzer0team.com/challenges/14/"
	bt_url = url+str(hash_message)
	driver.get(bt_url)
	driver.forward()

	sleep(10)

def main():
	webdriver_login()

if __name__ == '__main__':
	main()
