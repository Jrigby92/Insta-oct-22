from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
import time
from time import sleep
import random
from random import choice
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import selenium.webdriver.chrome.options
import json
from random import uniform
import urllib3
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from pylint import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException



 # Username:str: the instagram username
    # Password:str:  instagram password
    # login function is included in the class body

class InstagramBot:

    def __init__(self, username, password,):
        # self.set_chrome_options
        # self.driver = self.set_chrome_options()
        options = Options()
        # options.add_argument("--no-sandbox")
        # options.add_argument("--headless")
        # options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        # options.add_argument('--disable-gpu')
        

        self.driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        # self.driver = webdriver.Chrome(executable_path=r'./chromedriver', Options = chrome_options)
        print("Task 1")
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        sleep (5)
        # Clicking accept on cookies popup
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Only Allow Essential Cookies']"))).click()
        except TimeoutException:
            pass
        print("task 2")
        sleep(uniform(2,4))
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name=\"username\"]"))).send_keys(self.username)
        except TimeoutException:
            pass
        sleep(uniform(1,2))
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name=\"password\"]"))).send_keys(self.password)
        except TimeoutException:
            pass
        sleep(uniform(0,1))
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        except TimeoutException:
            pass


# sleep while logging in
        sleep(uniform(3,6))
    
# MINOR FUNCTIONS

    def randomisation_sleep_time (self):
        w =randint(0,10)
        if w <5:
            time.sleep(uniform(0.5,2))
            
        elif w > 5 < 8:
            time.sleep(uniform(1,3))
            
        else:
            time.sleep(uniform(4,12))
            
        
    
    
    def page_scroll_amount(self):
        # ensuring the program usually scrolls between 16 and 48 times, but has a range of 1 and 121 times. 
        sa = randint(0,100)
        if sa > 77 <98:
            a = randint(35,82)
        elif sa >98:
            a = randint(75,120)
        elif sa < 12:
            a = randint(1,16)
        else:
            a = randint(16,48)

        return(a)

    def identify_element_and_click(self, target_function, path_type, path):

        try:

        
            sleep(uniform(1,2))
            try:
                if path_type == 'xpath':
                
                    self.driver.find_element_by_xpath(path)\
                    .click()
            
                elif path_type == 'name':
                    self.driver.find_element_by_name(f'{path}')\
                    .click()
            
                elif path_type == 'class_name':
                    self.driver.find_element_by_class_name(f'{path}')\
                    .click() 
               
                elif path_type == 'css_selector':
                    self.driver.find_element_by_css_selector(f'{path}')\
                    .click()
            
                elif path_type == 'tag_name':
                    self.driver.find_element_by_tag_name(f'{path}')\
                    .click()
                
                print(f'{target_function} clicked succesfully')

            
            except NoSuchElementException:

                print(f'{target_function} failed to click')

            sleep(uniform(1,4))
        
        except ElementClickInterceptedException:
            pass


    def identify_elements_and_click(self, target_function, path_type, path, index):

        sleep(uniform(1,2))

        try: 
        
            try:
                if path_type == 'xpath':
                
                    self.driver.find_elements_by_xpath(path)[index]\
                    .click()
            
                elif path_type == 'name':
                    self.driver.find_elements_by_name(path)[index]\
                    .click()
            
                elif path_type == 'class_name':
                    self.driver.find_elements_by_class_name(path)[index]\
                    .click() 
            
                elif path_type == 'css_selector':
                    self.driver.find_elements_by_css_selector(path)[index]\
                    .click()
            
                elif path_type == 'tag_name':
                    self.driver.find_elements_by_tag_name(path)[index]\
                    .click()
            
                print(f'{target_function} clicked succesfully')
                
            
            except NoSuchElementException:
                pass

        except ElementClickInterceptedException:
            pass

            print(f'{target_function} failed to click')
            

        sleep(uniform(1,4))





# NATURAL BHEAVIOUR FUNCTIONS

    def browse_profile_after_having_landed(self):
        # sleeping after landing
        sleep(uniform(1,5))

        # setting amount of scrolls to do on page
        scroll_amount = randint(2,5)

        scrolls_executed =0

        # scrolling down profile
        while scrolls_executed < scroll_amount:
            scrolls_executed += 1
            # setting how many pixels to scroll
            s = randint(300,700)
            # executing scrolls 
            self.driver.execute_script(f"window.scrollBy(0,{s})")

            # sleeping random amounts of time, to emulating organic broswing activity
            self.randomisation_sleep_time()


            # POST LIKING: Chance of liking a post ratio -1
            z = randint(0,6)

            if z > 3:
                # liking a post from the main profile
                self.navigating_to_post_and_liking(scrolls_executed+2, scrolls_executed+4)
                sleep(uniform(1,3))

                if z > 4:
                    # 1 / 2 times, liking a post from the recommended posts at the bottom.

                    self.navigating_to_post_and_liking(0, 6)
                    sleep(uniform(1,5))
                    scrolls_executed = scroll_amount
                
                else:
                    scrolls_executed = scroll_amount



    def check_and_return_recent_activity(self):

        # clicking first popup after logging in

        self.identify_element_and_click('first login popup', 'xpath', '//*[@id="react-root"]/section/main/div/div/div/div/button')

        
        # clicking second pop up 
        self.identify_element_and_click('second login popup', 'xpath', '/html/body/div[4]/div/div/div/div[3]/button[2]')
        

        # Short random sleep after landing on newsfeed
        self.randomisation_sleep_time()

        # Clicking on recent activity
        self.identify_element_and_click('recent activity button', 'xpath', '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
        
        
        sleep(uniform(2,6))
        
        # Clicking one of the users in the recent activity drop down
        
        recent_user = randint(1,5)

        if recent_user == 1:
            self.identify_elements_and_click('first user in recent activity list', 'xpath', '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]', 0)

        if recent_user == 2:
            self.identify_elements_and_click('Second user in recent activity list', 'xpath', '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]', 0)
 
        if recent_user == 3:
            self.identify_elements_and_click('Third user in recent activity list', 'xpath', '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]', 0)
        
        if recent_user == 4:
            self.identify_elements_and_click('Fourth user in recent activity list', 'xpath', '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[4]/div[2]', 0)

        
        self.browse_profile_after_having_landed()
            





    def homepage_and_scroll(self):
        
        sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
            .click()
            sleep(uniform(1,4))
        except NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
            sleep(uniform(1,4))
        except NoSuchElementException:
            pass

        scroll = 0

        # ensuring the program usually scrolls between 16 and 48 times, but has a range of 1 and 121 times. 
        sa = self.page_scroll_amount()

        print(sa)
        
        while scroll < sa: # scroll 12, 16 times

            scroll += 1
            
            # setting the amount of pixels per scroll
            s = randint(600,1200)
            #  executing scroll
            self.driver.execute_script(f"window.scrollBy(0,{s})")

            # --------------
            # little function to randomise time gaps betwwen scrolls *emulating interest in certain posts whilst scrolling past others
            w =randint(0,10)
            if w <5:
                time.sleep(uniform(0,1))
            elif w > 5 < 8:
                time.sleep(uniform(1,3))
            else:
                time.sleep(uniform(7,17))

            # so more often than not, when the scrolling stops, the post in screen will be liked. 
                a = randint(0,200)
                if a <137:

                    self.identify_elements_and_click('homepage like button','xpath', '//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]/button', 0)
                    sleep(uniform(2,6))
                    
                    # occasionally clicking on the profile and scrolling + maybe liking another post.
                    p = randint(0,200)
                    if p < 64:

                    # identifying profile
                        profile = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[5]/header/div[2]/div[1]/div/span')[0]
                        print(f"trying to click profile, targeted element list {profile}")
                        try:
                        # clicking on profile link
                            profile.click()
                            # browsing profile, maybe liking
                            self.browse_profile_after_having_landed()

                            # ensuring function ends and program doesnt continue trying to scroll the homepage
                            scroll = sa
                            

                        except NoSuchElementException:
                            pass
            
                
                elif a >137 < 152:
                    # identifying profile
                    profile = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[5]/header/div[2]/div[1]/div/span')[0]
                    print(f"trying to click profile, targeted element list {profile}")
                    try:
                       # clicking on profile link
                        profile.click()
                        sleep(uniform(0.2,0.8))
                        profile.click()
                        sleep(uniform(1,3))
                        self.browse_profile_after_having_landed()
                        scroll = sa

                    except NoSuchElementException:
                        pass


        time.sleep(uniform(2,9))
                 
            
        
        s = randint(600,1200)
        self.driver.execute_script(f"window.scrollBy(0,{s})")
        sleep(uniform(3,7))

# Search 
    # def search(x):
    #     search_box=br.find_element_by_xpath("//input[@type='text']")
    #     search_box=br.find_element_by_xpath("//input[@class='pbgfb Di7vw ']")
    #     search_box.clear() 
    #     search_box.send_keys(str(x))
    #     time.sleep(sleeping)
    #  @@ -117,12 +111,7 @@ def change_ip():
    #     time.sleep(3)
    #     return()
 
# MINOR FUNCTIONS
    
    def ensuring_scrape_account_is_active(self):
        # scrape_accounts = ['amore.aesthetics','klccosmetics', 'kiss_aesthetics', 'goddessaestheticsmcr', 'm.i.a_aestheticsmcr', 'demijeanaesthetics', 'medical.aestheticsmcr', 'misshudsonaesthetics_', 'c.caesthetics', 'nicolelucia_aesthetics', 'lauren.cosmetic.aesthetics', 'nassifmedspauk', 'amicaaesthetics', 'luxe.aesthetics', 'facesbyakj']
        # print(f"len of sc {len(scrape_accounts)}")
        # Photo list 
        # scrape_accounts = ['pocahunitt']
        scrape_accounts = ['jallcockfoxphotography','photographybyzak', 'martinschoeller', 'shotby_andypate']
        a = len(scrape_accounts)
        
        # For as long as the follower box of the targetted scrape account cannot 
        # be located, elem = None
        elem = None
 
        # this will loop will keep running until an active scrape account 
        # (selected at random) is found. That account will then be assigned as 
        # return value of the function
        while not elem:
            try:
                b = randint(0, a-1)
                self.nav_user(scrape_accounts[b])
                sleep(uniform(1,3))
                elem = self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")
            except NoSuchElementException:
                del scrape_accounts[b]
                b = randint(0,a-1)
                self.nav_user(scrape_accounts[b])
                sleep(uniform(1,3))
                elem =self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")
                
        
        
        return(scrape_accounts[b])
        

    def nav_user(self, user):
        print("Task X")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.get('{}/{}/'.format(self.base_url, user))
        # sleep whilst user page loads
        sleep(uniform(3,5))
        

    def opening_followers_box(self):
        print("Task 2")
        followers_link = self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]")
        followers_link.click()

        sleep(uniform(2,4))



    def scrolling_followers(self):
        print("Task 3")
        driver = self.driver

        fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < randint(36,48): # scroll 12, 16 times
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(uniform(1,2))
            scroll += 1

        print("ended")



    def storing_followers_in_json(self):
        print("Task 4")
        
        dialog = self.driver.find_element_by_xpath("//div[contains(@role, 'dialog')]")
        # identifying user accounts from followers box
        names = dialog.find_elements_by_tag_name('a')
        # compiling accounts into a list
        to_follow = [name.text for name in names if name != ''][2:]
        
        # filtering list from empty values
        to_follow = list(filter(None, to_follow))

        print(to_follow)

        sleep(uniform(2,4))

        # exporting list to json 
        with open(f'to_follow_{self.username}.json', 'w') as f:
             json.dump(to_follow, f)
    

    def storing_accounts_user_is_following_to_python_list_called_following(self):
        # Navigating to users own page
        self.nav_user(self.username)
        sleep(uniform(1,4))
        
        # clicking on following box
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(uniform(1,4))

        # Scrolling following box
        following_box  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < randint(220,280): # scroll 12, 16 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', following_box)
            # self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', following_box)
            sleep(uniform(1,2))
            scroll +=1
        
        # STORING ACCOUNTS USER IS "FOLLOWING" INTO PYTHON LIST

        dialog = self.driver.find_element_by_xpath("//div[contains(@role, 'dialog')]")
        # identifying user accounts from followers box
        names = dialog.find_elements_by_tag_name('a')
        # compiling accounts into a list of accounts which are currently followed by user
        following = [name.text for name in names if name != ''][2:]
        
        # filtering list of empty values
        following = list(filter(None, following))

        return(following)

    def generating_to_follow_list(self):
        user_to_scrape = self.ensuring_scrape_account_is_active()
        self.nav_user(user_to_scrape)
        self.opening_followers_box()
        self.scrolling_followers()
        self.storing_followers_in_json()

    def navigating_to_post_and_liking(self, first_post, last_post):
            post = self.driver.find_elements_by_xpath('//a[contains(@href,"/p/C")]')
        # extracting the full href from each element in the 'post' list
            links = [elem.get_attribute('href') for elem in post]
        # Navigating and liking one of the first 3 values in the links list (userspost) at random
            try:
                self.driver.get(links[randint(first_post,last_post)].format(self.base_url))
                sleep(uniform(1,3))
                like_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                like_button.click()
            except IndexError:
                pass

    


    
# PRIMARY BUILDING BLOCK FUNCTIONS I.E. BASE FUNCTIONS



    def like(self):

        print("Task B")
        
        # PUTTING POST LINKS IN LIST
        # Finding post elements by href into a list / using list to navigate to specificposts in clicking_and_liking function    
        post = self.driver.find_elements_by_xpath('//a[contains(@href,"/p/C")]')
        # extracting the full href from each element in the 'post' list
        links = [elem.get_attribute('href') for elem in post]


        def navigating_to_post_and_liking(first_post, last_post):
        # Navigating and liking one of the first 3 values in the links list (userspost) at random
            try:
                self.driver.get(links[randint(first_post,last_post)].format(self.base_url))
                sleep(uniform(1,3))
                like_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                like_button.click()
            except IndexError:
                pass

        sleep(uniform(1,7))
 
        #  first like
        navigating_to_post_and_liking(1,4)
        # sleep before next like
        sleep(uniform(1,3))


        # Second like/ 50% chance of happening
        a = randint(1,3)
        if a == 2:
            navigating_to_post_and_liking(4,8)
        # sleep before next like
        sleep(uniform(2,4))

        # Third like/ 40% chance of happening
        b = randint(1,6)
        if b >= 4:
            navigating_to_post_and_liking(8,12)
        


    def follow_and_like(self):
        
        # opening users from to_follow.json and followed.json lists
        # storing users in python lists
        with open(f"to_follow_{self.username}.json","r") as f:
            to_follow = json.load(f)

        print(f"Length of tf list: {len(to_follow)}")

        with open(f"followed_{self.username}.json","r") as f:
            followed = json.load(f)
        
        print(f"Followed_list_length{len(followed)}")

        # Running the predefined function to scrape all accounts being followed by user 
        # and storing them into a list called following
        following = self.storing_accounts_user_is_following_to_python_list_called_following()
        # printing that list
        print(f"Following_list-length{len(following)}")

        # Concatonating all accounts user is following (maybe not by the bot)
        # with all accounts ever followed by the bot
        # (*)to ensure program does try and follow anyone whoes already followed)
        # and storing all in a new followed list
        not_to_follow = following + followed
        
        # removing duplicates from the new followed list
        not_to_follow = list(dict.fromkeys(followed))

        # Making sure that no account in the to_follow list is in the not_to_follow list
        # i.e. this will delete any account which is in the not_to_follow list, from the to_follow list. 
        to_follow = [x for x in to_follow if x not in not_to_follow]

        # printing new length to_follow list
        print(f"Filtered length of tf list: {len(to_follow)}")

        # function to make sure the follow list is no greater than 150 (if it is, it will randomly delete users from thestart and end of the list)
 
        # setting the amount of people to follow. 
        amount_to_follow_per_day = randint(120,175)

        b = randint(0,2)

        while len(to_follow)> amount_to_follow_per_day:
            if b ==0:
                to_follow.pop(0)
            else:
                del to_follow[-1]

        print(len(to_follow)) 
        
        # function to ensure new users to follow are found, if initial list is less than 120-175. 
        attempt = 1
        while len(to_follow) < amount_to_follow_per_day:
            attempt+=1
            self.generating_to_follow_list()
            # loading new to follow list from json
            with open(f"to_follow_{self.username}.json","r") as f:
                additional_follow_list = json.load(f)
            # filtering new list from accounts which should not be refollowed
            additional_follow_list = [x for x in additional_follow_list if x not in not_to_follow]

            print("generating and concatonating additional tf list")
            to_follow = additional_follow_list + to_follow
            
            # filtering new list from duplicte accounts
            to_follow = list(dict.fromkeys(to_follow))

        b = randint(0,2)
        while len(to_follow)>amount_to_follow_per_day:
            if b ==0:
                to_follow.pop(0)
            else:
                del to_follow[-1]

        print(f"New tf list length {len(to_follow)}") 
        
        # Now the to_follow list should be filtered and have a length of 150 values/accounts
# ------------------------------------------------------------------------------------
        # using a as a variable which inclines by 1 each timea user is followed
        # to ensure program only runs follow function for as many times
        # as their is accounts in the to_follow list
        
        a=0

        while a < 150:

            a+=1
            
            # If an account deletes itself since being added to the to_follow list, and tf list becomes  <150
            # this will prevent program from crashing. because the while loop needs to iterate 150 times. 
            if len(to_follow)==0:
                to_follow.append('https://google.com')

            user1 = [to_follow[0]]

            self.nav_user(to_follow[0])
            sleep(uniform(3,5))
            # locating and clicking follow buton
            print("Task A")
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
                # appending followed user to followed list
                followed.extend(user1)
 
                sleep(uniform(1,4))
                   
                self.like()
                   

                # saving the new followed list
                with open(f"followed_{self.username}.json","w") as f:
                    json.dump(followed, f, indent=1)
                
                # deleting followed user from to_follow list
                # self.driver.find_element_by_class_name("//div[@class='eLAPa']").click
                # print("yep")

                
                a = randint(1,10)

                # 1/10 times program will wait 7-11(ish) minutes before finding a new user
                # 1/10 times program will wait 30-90 seconds before finding a new user
                # 8/10 times it will wait 1.5-5(ish) minutes
                if a > 9:
                    sleep(uniform(420,686))
                elif a < 2:
                    sleep(uniform(30,90))
                else:
                    sleep(uniform(123,264))
            except NoSuchElementException:
                pass

            del to_follow[0]
                

    def unfollow(self):
        
        following = self.storing_accounts_user_is_following_to_python_list_called_following()
        
        # uploading all accounts ever followed by this program from json to python list
        with open(f"followed_{self.username}.json","r") as f:
            followed = json.load(f)
        
        # Cross checking following and followed lists for duplicate values
        # to identify accounts that the program has followed in the past, 
        # and which the user is still following 
        # and therefore needs to be unfollowed. 
        # adding those accounts into an unfollow list 

        to_unfollow = [item for item in following if item in followed]

        print(to_unfollow)
        
        # reversing to_unfollow list to ensure that accounts which were followed first are unfollowed first
        
        to_unfollow.reverse()
        print(to_unfollow)

        # BEGGINING TO UNFOLLW EACH USER IN LIST
        try:
            while len(to_unfollow) > 0:
                # navigating to top user (user followed longest ago) in unfollow list
                if to_unfollow[0]=="":
                    del to_unfollow[0]

                self.nav_user(to_unfollow[0])

                # 1/10 times program will wait 11-26 secs before clicking unfollow
                # 9/10 times it will wait 3-8
                a = randint(1,11)
                if a > 9:
                    sleep(uniform(11,26))
                else:
                    sleep(uniform(3,8))

                # Finding and clicking unfollow button
                try:
                    self.driver.find_element_by_class_name("_6VtSN").click()
                    sleep(uniform(1,3))
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                
                except NoSuchElementException:
                    pass 
                
                # Because the some accounts have a different element name for the unfollow button
                try:
                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div[2]/button').click()
                    sleep(uniform(1,3))
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                
                except NoSuchElementException:
                    pass 


                try:
                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button').click()
                    sleep(uniform(1,3))
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                
                except NoSuchElementException:
                    pass 

                del to_unfollow[0]
                with open(f"to_unfollow_{self.username}.json","w") as f:
                    json.dump(to_unfollow, f, indent=1)
        except TypeError:
            pass

        sleep(uniform(2,4))



# SECONDARY BUILDING BLOCKS // COMPILATIONS OF PRIMARY FUNCTIONS*

    def follow_cycle(self):

        # To find out run timelength
        start = time.time()
        print(f"Start time of follow cycle {start}")

        # TO RANDOMISE START UP CYCLE
        x = 100
        if x < 28:
            self.check_and_return_recent_activity()
        
        elif x > 28 <72:

            self.homepage_and_scroll()

        else:
            pass

        account_to_scrape = self.ensuring_scrape_account_is_active()

        self.nav_user(account_to_scrape)
        self.opening_followers_box()
        self.scrolling_followers()
        self.storing_followers_in_json()
        self.follow_and_like()

        end = time.time()
        print(f"End time of follow cycle {end}")
        print(f"Runtime of the program is {end - start}")


# ACTIVE FUCTIONS
    
    def follow_unfollow(self):

        # to ensure the program runs continuously 
        while True:
            
            # Follow cycle 1
            self.follow_cycle()

            # follow cycle 2
            self.follow_cycle()
            
            # RANDOM BREAK between 43 minutes and 64 minutes (ish)
            sleep(uniform(2556,3850))

            # follow cycle 3
            self.follow_cycle()
            
            # unfollow cycle
            self.unfollow()

            #RANDOM BREAK between 8 and 22 minutes
            sleep(uniform(496,1388))



if __name__ == '__main__':
    

    ig_bot = InstagramBot('username goes in this string', 'password goes in this string')

    ig_bot.follow_cycle()