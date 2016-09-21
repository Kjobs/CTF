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

def message_sha1_decrypt(cipher):
  #进入相关网站进行查询得到解密信息
	url = "http://hashtoolkit.com/reverse-hash?hash="+cipher

	new_driver = webdriver.Chrome()
	new_driver.get(url)

	info = new_driver.find_element_by_xpath("//span[@title='decrypted sha1 hash']").text
	return info

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

	#点击进入challenge56
	driver.get("https://ringzer0team.com/challenges/56")
	driver.forward()

	#获取message信息并利用hash_info函数进行加密
	message = driver.find_element_by_xpath("//div[@class='message']").text
	cipher_message = message_match(message)
	
	#进入http://hashtoolkit.com/?utm_source=md5&utm_medium=r&utm_campaign=md5网站进行sha1密文查询
	#构造url如下
	url = "http://hashtoolkit.com/reverse-hash?hash="+str(cipher_message)
	#利用selenium进入网站进行查询
	driver.get(url)
	driver.forward()
	send_message = driver.find_element_by_xpath("//span[@title='decrypted sha1 hash']").text

	#发送信息给目标网址
	url = "https://ringzer0team.com/challenges/56/"
	bt_url = url+str(send_message)
	driver.get(bt_url)
	driver.forward()

	sleep(10)

def main():
	webdriver_login()

if __name__ == '__main__':
	main()
