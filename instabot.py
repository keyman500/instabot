from selenium import webdriver
from time import sleep
from Secure import user,password
import requests
class Instabot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
        self.driver.get("https://instagram.com")
        self.username = username
        self.password = password
        sleep(2)

    def login(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(self.username)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button").click()
        sleep(10)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    #this funtion takes the main picture on the first post after you have loged in.
    def takepic(self):
        sleep(10)
        firstpic = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div")
        firstpic.click()
        imgname = "firstpic"
        imgs = firstpic.find_elements_by_tag_name("img")
        x=1
        for p in range(2):
            link = imgs[p].get_attribute("src")
            reponse = requests.get(link)
            file = open(imgname + str(x) + ".png","wb")
            file.write(reponse.content)
            file.close()
            x+=1
    #this function is used too download the first post on your instagram feed after you have loged in.
    def takefirstpost(self):
        sleep(10)
        firstpic = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div")
        firstpic.click()
        imgname = "firstpic"
        imgs = firstpic.find_elements_by_tag_name("img")
        x = 1
        for img in imgs:
            link = img.get_attribute("src")
            reponse = requests.get(link)
            file = open(imgname + str(x) + ".png","wb")
            file.write(reponse.content)
            file.close()
            x+=1
    def downloaduser(self,user):
        x = 1
        imgnames = []
        self.getuser(user)
        sleep(3)
        SCROLL_PAUSE_TIME = 2.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        counter = 0
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                x = self.downloadimgs(counter,user,x,imgnames)
                break
            last_height = new_height
            counter+=1
            if counter % 1 == 0:
                x = self.downloadimgs(counter,user,x,imgnames)

    #this function is used too download images after a scroll is made. it is a helper function for download user.
    def downloadimgs(self,counter,user,x,imgnames):
        imgname = user
        allpics = self.driver.find_element_by_xpath("//html/body/div[1]/section/main/div/div[3]")
        imgs = allpics.find_elements_by_tag_name("img")
        print(allpics)
        print("downloading" + "  " + str(counter))
        for img in imgs:
            link = img.get_attribute("src")
            if link not in imgnames:
                reponse = requests.get(link)
                file = open(imgname + str(x) + ".png", "wb")
                file.write(reponse.content)
                file.close()
                x += 1
            imgnames.append(link)
        return x
        
    #this function will download all images currently loaded on the display
    def downloadloaded(self, user):
        self.getuser(user)
        allpics = self.driver.find_element_by_xpath("/html/body")
        imgs = allpics.find_elements_by_tag_name("img")
        x = 1
        imgname = user
        for img in imgs:
            link = img.get_attribute("src")
            reponse = requests.get(link)
            file = open(imgname + str(x) + ".png", "wb")
            file.write(reponse.content)
            file.close()
            x += 1
    #this is a heaper funtion used too go to a user's profile page
    def getuser(self,user):
        sleep(4)
        self.driver.get("https://instagram.com"+"/"+user)




