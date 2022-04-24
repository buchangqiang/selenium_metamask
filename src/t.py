import time
import undetected_chromedriver as uc
if __name__=="__main__":
    options = uc.ChromeOptions()
    #C:\work_code\selenium_metamask\chromedriver.exe

    driver = uc.Chrome()
    
    driver.implicitly_wait(40)
    driver.get('https://portal.zksync.io/')
    print('...........')
    time.sleep(40)