from os import write
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
def get_ans(s):
    no=[]
    a=s
    for i in a.split():
        if i.isdigit():
            no.append(int(i))
    
    if('subtract' in s):
        return (no[0]-no[1])
    elif('add' in s):
        return (no[0]+no[1])
    elif('first' in s):
        return (no[0])
    elif('second' in s):
        return (no[1])
def moodle():
    driver=webdriver.Chrome()
    driver.get('https://moodle.iitd.ac.in/login/index.php')
    login_id=driver.find_element_by_xpath('//*[@id="username"]')
    login_id.send_keys('Your Id')
    password=driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('Your password')
    captcha_statement=driver.find_element_by_xpath('//*[@id="login"]').text
    a=get_ans(captcha_statement)
    write_captcha=driver.find_element_by_xpath('//*[@id="valuepkg3"]')
    write_captcha.send_keys(a)
    log_in=driver.find_element_by_xpath('//*[@id="loginbtn"]')
    log_in.click()
