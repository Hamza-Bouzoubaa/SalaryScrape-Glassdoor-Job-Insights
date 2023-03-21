from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Get the website using the Chrome webbdriver<
def openWebdriver() :
    global browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome()


def GetInfo(Job_title,Amount):
    openWebdriver()
    browser.maximize_window()
    browser.get("https://www.glassdoor.com/Job")  #open site 
    sleep(1)
    Navigtion_bar = browser.find_element("xpath","//*[@id='sc.keyword']") #Navigation bar
    Navigtion_bar.click()  #click on it 
    sleep(1)
    Navigtion_bar.send_keys("data analyst")  #position to scrap
    Navigtion_bar.send_keys(Keys.ENTER)
    #sleep(100)
    for i in range (0,Amount+1,1):
        print(i%30+1)
    
        Description = browser.find_element("xpath","//*[@id='MainCol']/div[1]/ul/li["+str(i%30+1)+"]/div[2]/a/span")
        print("//*[@id='MainCol']/div[1]/ul/li["+str(i%30+1)+"]/div[2]/a/span")
        Description = Description.text

        try:
            Salary = browser.find_element("xpath","//*[@id='MainCol']/div[1]/ul/li["+str(i%30+1)+"]/div[2]/div[3]/div[1]/span")
            Salary = Salary.text

        except:
            Salary = "No Salary available"

        print(Description)
        print(Salary)
        print("_____")


        if (i%30==1 and i!=1):
            print("List finished")
            Next_Page = browser.find_element("xpath","//*[@id='MainCol']/div[2]/div/div[1]/button[7]")
            Next_Page.click()
            sleep(5)
            try:
                Pop_up = browser.find_element("xpath","//*[@id='JAModal']/div/div[2]/div[2]/div/div/div[1]/h3").is_displayed()
                if (Pop_up==True):
                    print("POPUP")
                    Pop_up = browser.find_element("xpath","//*[@id='JAModal']/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/button")
                    Pop_up.send_keys(Keys.ESCAPE)
            except:
                print("No POPUP")

                
                

    sleep(10000)
    browser.close()
    browser.quit()


GetInfo("Software engineer",35)
