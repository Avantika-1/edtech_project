import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options

def test_open_testalogin():
    #Option class -> customize browser behaviour during automation testing
    #Browser work on two mode :-> 1. headless means no ui 2. UI
    #we can 100 of option to add before starting like incognito mode

    edge_option = Options()
  #  edge_option.add_argument("--window-size=1920x1080")
    edge_option.add_argument("--inprivate")  #incognito will use for chrome
    edge_option.add_argument("--disable-infobars") # to disable the "ex-browser is automated"
   # edge_option.add_argument("--headless") #to run code into headless mode where no UI will launch pros:-> low memomey allocation, fast
    driver = webdriver.Edge(edge_option)
    driver.get("https://preprod.testaonline.com/signin")

    '''
    
    
     
  
    print(driver.title)
    assert driver.title == "Testa | Dev"
    print(driver.session_id)
    
    '''
    time.sleep(10)

