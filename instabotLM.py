'''
v1.0.0
(2021)
Bot made by: Lucas Martinez
Github: @martinezlucas98
Project repository: https://github.com/martinezlucas98/instabotLM
'''

import json
from getpass import getpass
import time
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

CHROMEDRIVERPATH = "./chromedriver"
CHROMEDRIVERSERVICE = Service(CHROMEDRIVERPATH)
BOTINFO = '''v1.0.0
(2021)
Bot made by: Lucas Martinez
Github: @martinezlucas98
Project repository: https://github.com/martinezlucas98/instabotLM
'''
COMMENTINTERVAL = 120
WAITTIME = 5
driver = any


def login(uname, pwd):

    wait = WebDriverWait(driver, WAITTIME)

    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "username")
        )
    ).send_keys(uname)

    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "password")
        )
    ).send_keys(pwd)

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF")
        )
    ).click()
    
    print("Login: OK!")


def str_tags(tags):
    tag_str = ""
    for tag in tags:
        tag_str += '@'+tag+" "

    return tag_str


def comment_post(url, tags, quantity, like, follow):
    driver.get(url)
    comment = str_tags(tags)
    sleep_time = COMMENTINTERVAL+random.randint(1, 10)
    wait = WebDriverWait(driver, WAITTIME)

    if (follow):
        print("Trying to follow user...")
        try:
            follow_div = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "bY2yH") # not following yet
                )
            )
            follow_div.find_element(By.XPATH, "//button[1]").click() # "sqdOP yWX7d y3zKF"
            print("Follow = OK!")
        except:
            print("You already follow this user")

    if (like):
        print("Trying to like post...")
        try:
            like_section = wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "fr66n")
                )
            )

            like_btn = like_section.find_element(By.TAG_NAME, "button")
            try:
                like_btn.find_element(
                    By.XPATH, "//div[1]/span[1]/*[local-name()='svg' and @fill='#ed4956']")  # /svg[@color='#ed4956']
                print("You already liked this post")
            except:
                like_btn.click()
                print("Like = OK!")

        except:
            print("Error? :: Like exception")

    try:
        print("The bot is commenting...")
        for i in range(0, quantity):
            wait.until(
                EC.element_to_be_clickable(  # EC.presence_of_element_located(
                    (By.XPATH,
                     "//textarea[@data-testid='post-comment-text-area']")
                )
            ).click()

            driver.find_element(
                By.XPATH, "//textarea[@data-testid='post-comment-text-area']").send_keys(comment)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//button[@data-testid='post-comment-input-button']")
                )
            ).click()

            # sleep before next post just so instagram bot hunter (if it exists) doesnt kill us so fast
            time.sleep(sleep_time)

    except Exception as e:
        print("Exception location: for _ in range(0, quantity) with quantity = "+str(quantity))
        print("An ERROR has occured:")
        print("INFO: Please check if the URL is a valid URL")
        print(e)


def main():
    global driver
    global COMMENTINTERVAL
    global WAITTIME

    args = sys.argv[1:]
    if (len(args)):
        COMMENTINTERVAL = float(args[0])

        if (len(args)>1):
            WAITTIME = float(args[1])

    has_error = False

    print(BOTINFO)
    print("\n\nConfigurations:")
    print("\tComment interval: "+str(COMMENTINTERVAL)+"seconds")
    print("\tPage load wait time: "+str(WAITTIME)+"seconds\n")

    pwd = getpass()
    f = open('./options.json', 'r')
    data = json.load(f)

    data["username"] = data["username"].lower()
    data["follow"] = data["follow"].lower()
    data["like"] = data["like"].lower()

    for i in range(0, len(data["tags"])):
        data["tags"][i] = data["tags"][i].lower()

    like = True
    follow = True

    if (data["like"] == "no"):
        like = False

    if (data["follow"] == "no"):
        follow = False

    f.close()
    try:
        try:
            driver = webdriver.Chrome(service=CHROMEDRIVERSERVICE)
        except:
            # For older versions of Selenium
            driver = webdriver.Chrome(CHROMEDRIVERPATH)
            
        driver.get("https://instagram.com")
        # driver.maximize_window()
    except Exception as e:
        print("Exception location: webdriver")
        print("An ERROR has occured:")
        print(e)
        has_error = True

    if (not has_error):
        try:
            login(data["username"], pwd)
            wait = WebDriverWait(driver, WAITTIME)

            # Wait until login completes (if /direct/inbox/ href exist then you are logged in)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//a[@href="/direct/inbox/"]')
                )
            )

            comment_post(data["postUrl"], data["tags"],
                         data["comments"], like, follow)

            print("Task ended successfully!")
        except Exception as e:
            print("Exception location: login/comment")
            print("An ERROR has occured:")
            print(e)
            has_error = True
            # driver.quit()

    driver.quit()


if __name__ == "__main__":
    main()
