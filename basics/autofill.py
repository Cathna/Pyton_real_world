##################################
## Created by: William Caudwell ##
## Date: 14/10/2022             ##
## For use of UAT Technicians   ##
##                              ##
##################################

#Script uses Selenium and Pandas
#to install using python use the follow commands
#pip install selenium
#pip install pandas


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#URL for the Results Service for Candidates, replace with UAT version

page_url = "https://candidates.cambridgeenglish.org/Members/Login.aspx?M=None"

#CSV file data imported into a dataframe called df, this must point to where your CSV file is
df = pd.read_csv("C:/Users/caudww/Downloads/Examples.csv")

#Webdriver, Firefox instructioncan be found https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox.html
#Webdriver, Edge instructions can be found https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
#Webdriver for Chrome, available from https://chromedriver.chromium.org/downloads, ensure correct version downloaded for the version of Chrome being used
#The below must point to where the webdriver is stored
driver = webdriver.Chrome('C:/Users/caudww/Downloads/chromedriver_win32/chromedriver.exe')


#Class to scrol to bottom of page
def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

def enter_text(driver,element_class,answer):
       fill = driver.find_element(By.NAME,element_class)
       fill.send_keys(answer)
        
#Text box IDs defined and entered into a list, Ids were found by loading the page and inspecting the class elements
ID_Number_input = "txbIdNumber"
Secret_Number_input = "txbSecretNumber"
Email_input = "txbEmailAddress"
Confirm_Email_input = "txbConfirmEmailAddress"
Password_input = "txbPassword"
Confirm_Password_input = "txbPasswordConfirm"

elements = [ID_Number_input,Secret_Number_input,Email_input,Confirm_Email_input,Password_input,Confirm_Password_input]


#Function that loops through the dataframe, using the total number of entries for the number of loops
for user_id in range(len(df)):
   time.sleep(1)     
   driver.get(page_url)#Browser opened and page loaded
   driver.maximize_window()#window maximised
   scroll_to_bottom(driver)#does what it says
   time.sleep(1)
   #finds the register button and clicks it
   reg = driver.find_element(By.ID,"hlRegister")
   reg.click()
#Candidate details are stored for each entry and added to a list
   ID_num = df["ID Number"][user_id]
   Sec_num = df["Secret Number"][user_id]
   Em_in = df["Email Address"][user_id]
   Em_con = df["Email Address"][user_id]
   Ps_in = df["Password"][user_id]
   Ps_con = df["Password"][user_id]
   text_answers = [ID_num,str(Sec_num),Em_in,Em_con,Ps_in,Ps_con]
#The test inputs are looped through and matching candidate details entered in text boxes
   for element in range(len(elements)):
        enter_text(driver,elements[element],text_answers[element])
#Scrolls to bottom and click the I agree radio button and submit button
   scroll_to_bottom(driver)
   time.sleep(1)
   tag = driver.find_element(By.ID,"rdoAgree")
   tag.click()
   sub = driver.find_element(By.ID,"btnSubmit")
   sub.click()
   time.sleep(2)     
  
