from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys

# Get the website using the Chrome webbdriver<
def openWebdriver() :
    global browser
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome()

def OpenSite(jobTitle):
    openWebdriver()
    browser.maximize_window()
    url = "https://www.glassdoor.com/Job"
    browser.get(url)  #open site 
    sleep(1)
    Navigtion_bar = browser.find_element("xpath","//*[@id='sc.keyword']") #Navigation bar
    Navigtion_bar.click()  #click on it 
    sleep(1)
    Navigtion_bar.send_keys(jobTitle)  #position to scrap
    Navigtion_bar.send_keys(Keys.ENTER)
    #sleep(100)

def CatchSignUpPopUp():
    try:
        Pop_up = browser.find_element("xpath","//*[@id='JAModal']/div/div[2]/div[2]/div/div/div[1]/h3").is_displayed()
        if (Pop_up==True):
            Pop_up = browser.find_element("xpath","//*[@id='JAModal']/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/button")
            Pop_up.send_keys(Keys.ESCAPE)
        return True
    except:
        return False


def findElement(num,i):

    if (num == 1):
        toFind = "//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]/div[2]/div[3]/div[1]/span"

    if (num ==2):
        toFind = "//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]/div[2]/a/span"

    if (num ==3):
        toFind ="//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]/div[2]/div[2]/span"

    if (num==4):
        toFind = "//*[@id='JobDescriptionContainer']" #JobDescription
        

    if (num== 5):
        toFind = '//*[@id="MainCol"]/div[1]/ul/li['+str(i)+']/div[1]/span' #rating

    if (num ==6):
        toFind ="//*[@id='EmpBasicInfo']/div[1]/div/div[3]/span[2]" #Industry

    if (num ==7):
        toFind = "//*[@id='EmpBasicInfo']/div[1]/div/div[1]/span[2]"  #size

    if (num ==8):
        toFind = "//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]/div[2]/div[1]/a/span"  #company  
    
    if (num==9):
        toFind = "//*[@id='EmpBasicInfo']/div[1]/div/div[2]/span[2]"  #Founded

    if (num==10):
        toFind = "//*[@id='EmpBasicInfo']/div[1]/div/div[6]/span[2]"    #Revenue

    try:

        Element = browser.find_element("xpath",toFind)
        Element = Element.text
    except:
        Element = -1
    
    return Element

def TurnPage():
    try:
        PageTurner = browser.find_element("xpath","//*[@id='MainCol']/div[2]/div/div[1]/button[7]")
        PageTurner.click()
        return True
    
    except:
        return False


def scraping(Amount):
    data = [["Company","Salary","JobTitle","Location","JobDescription","Rating","Industry","size","Founded","Revenue"]]
    for i in range (1,Amount+1+int(Amount//31),1):
        k = i%31
        
        if (k==0 and i!=0):
             TurnPage()
        try:
            JobInstance =  browser.find_element("xpath","//*[@id='MainCol']/div[1]/ul/li["+str(k)+"]")
            CatchSignUpPopUp()
            JobInstance.click()
            sleep(4)
            Salary = findElement(1,k)
            JobTitle = findElement(2,k)
            Location = findElement(3,k)
            JobDescription = findElement(4,k)
            Rating = findElement(5,k)
            Industry = findElement(6,k)
            size = findElement(7,k)
            Company = findElement(8,k)
            Founded = findElement(9,k)
            Revenue = findElement(10,k)



            data.append([Company,Salary,JobTitle,Location,JobDescription,Rating,Industry,size,Founded,Revenue])
            print(i,k)
        except:
            print(CatchSignUpPopUp())
            print("Error")

    return data





def GetInfo(Job_title,Amount):
    OpenSite(Job_title)
    data = scraping(Amount)    
    #sleep(1000)
    browser.close()
    browser.quit()
    print("closed")
    return pd.DataFrame(data)


