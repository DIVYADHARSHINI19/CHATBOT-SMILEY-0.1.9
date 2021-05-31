from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



## PLAYING AUDIO
def audio():

    song = input("Enter song name : ")
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    driver.get("https://gaana.com/")
    print("playing", song)


    def playsong():
        search = driver.find_element_by_id("sb")
        search.send_keys(song)
        search.send_keys(Keys.ENTER)
        sleep(1)
        find = driver.find_element_by_class_name("img")
        find.click()

    playsong()

