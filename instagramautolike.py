from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(7)
username = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
#You must enter your username in this field
LoginUsername = "------"
username.send_keys(LoginUsername)
password = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
#You must enter your password in this field
LoginPassword = "------"
password.send_keys(LoginPassword)
LoginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
LoginButton.click()
time.sleep(7)

#To the pass instagram notification
not_now = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
if not_now is not None:
    not_now.click()
    time.sleep(7)

#To the pass instagram notification
for i in range(4,7):
    try:
        close_notifications = browser.find_element_by_xpath("/html/body/div[{}]/div/div/div/div[3]/button[2]".format(i))
        break
    except:
        None

close_notifications.click()
time.sleep(5)
input_area = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")

#Enter the username of the person whose photos you want to like here.
input_area.send_keys("------")
time.sleep(4)
profile = browser.find_element_by_css_selector(".-qQT3")
profile.click()
time.sleep(7)
open_photo = browser.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w")
open_photo.click()
time.sleep(7)
#Like and skip to next photo until all photos are liked.
while True:
    like = browser.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
    like.click()
    time.sleep(2)
    try:
        next = browser.find_element_by_css_selector(".l8mY4.feth3")
        next.click()
        time.sleep(6)
    except:
        break

browser.close()
