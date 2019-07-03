from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from time import sleep

def waitdriver(driver, xmlpath):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xmlpath))
    )

def whiledriver(driver, xmlpath):
    load_cnt = 0
    while(load_cnt<3):
        try:
            element = waitdriver(driver, xmlpath)
            return element
        except:
            load_cnt += 1
            print("Reconnecting... : "+str(load_cnt))
    if(load_cnt>=3):
        print("Reconnecting Error!")
        driver.quit()
        return False


driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://www.jobkorea.co.kr/recruit/joblist?menucode=duty')

career_btn = whiledriver(driver, '//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[3]/dt')
if(career_btn == False):
    driver.quit()
else:
    career_btn.click()

driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[3]/dd/div[1]/ul[1]/li[1]/label').click()
driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[4]/dt').click()
driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[4]/dd/div[1]/ul/li[5]/label/span/span').click()
driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dt').click()
driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[3]/label').click()
driver.find_element_by_xpath('//*[@id="duty_step2_10016_ly"]/li[1]').click()
driver.find_element_by_xpath('//*[@id="dev-btn-search"]').click()
sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select('#dev-gi-list > div > div.tplList.tplJobList > table > tbody')
trs = tbody[0].findAll('tr')
for tr in trs:
    tds = tr.findAll('td')
    #기업정보 가져오기
    a0 = tds[0].find('a')
    u = str(a0.get('href'))
    company_url = "http://www.jobkorea.co.kr"+u
    logo = ""
    strings = u.split('/C/')
    if(len(strings) == 2):
        
    print(str(len(strings))+" : ", end = "")
    print(strings[1])

driver.quit()

'''
koreab2b
http://img.jobkorea.co.kr/trans/c/200x80/k/o/JK_Co_koreab2b.png
http://img.jobkorea.co.kr/Images/Logo/160/g/a/gabia_160.gif
http://img.jobkorea.co.kr/Images/Logo/160/w/o/woowahan_160.gif
/Recruit/Co_Read/C/gabia
/Recruit/Co_Read/C/woowahan
'''