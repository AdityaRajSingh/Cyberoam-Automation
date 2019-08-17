from selenium import webdriver
import sys

webbrowser = webdriver.Firefox()
webbrowser.get("https://172.16.1.1:8090/httpclient.html")
search_form_password = None
search_form_username = None
while search_form_password == None or search_form_username == None:
    search_form_username = webbrowser.find_element_by_name('frmHTTPClientLogin').find_element_by_class_name('maindiv').find_element_by_class_name('datablock').find_element_by_class_name('tablecss').find_element_by_id('usernametxt').find_element_by_name('username')
    search_form_password = webbrowser.find_element_by_name('frmHTTPClientLogin').find_element_by_class_name('maindiv').find_element_by_class_name('datablock').find_element_by_class_name('tablecss').find_element_by_name('password')
search_form_username.send_keys(open(r"username.txt",'r').read())
search_form_password.send_keys(open(r"password.txt",'r').read())
search_form_submit = webbrowser.find_element_by_name('frmHTTPClientLogin').find_element_by_class_name('maindiv').find_element_by_class_name('datablock').find_element_by_class_name('tablecss').find_element_by_name('btnSubmit')
search_form_submit.click()
webbrowser.close()
sys.exit(0)
