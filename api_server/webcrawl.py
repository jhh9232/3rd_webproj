from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
#import requests as req

from time import sleep

import json


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

# def PageLength(driver, xmlpath):
#     lis = driver.find_elements_by_xpath(xmlpath)
#     for li in lis:
#         print("a")
#     return len(lis)

def PageLength(driver):
    res_len = whiledriver(driver, '//*[@id="anchorGICnt_1"]/li[1]/button/span/em').text
    res_len = res_len.replace(" ", "")
    res_len = res_len.replace("건","")
    res_len = res_len.replace("(","")
    res_len = res_len.replace(")","")
    res_len = res_len.replace(",","")
    res_len = int(res_len)
    return res_len

def parse_data(driver, datas = []):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.select('#dev-gi-list > div > div.tplList.tplJobList > table > tbody')
    trs = tbody[0].findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        #기업정보 가져오기
        a0 = tds[0].find('a')
        company_url = "http://www.jobkorea.co.kr"+str(a0.get('href'))
        #기업로고 가져오기
        # res=req.get(company_url)
        # com_html = BeautifulSoup(res.text,"html.parser")
        # div1 = com_html.select('body > div.company-wrap > div.company-header > div.company-header-container')
        # div2 = div1[0].find('div',{"class":"logo"})
        # if(div2 == None):
        #     logo = None
        # else:
        #     logo = div2.find('img').get('src')
        # print(logo)

        #채용정보 가져오기
        a1 = tds[1].find('a')
        recruit_url = "http://www.jobkorea.co.kr"+str(a1.get('href'))

        #상세정보
        p = tds[1].find('p',{"class":"etc"})
        spans = p.findAll('span')

        #몇시까지
        span = tds[3].find('span',{"class","date dotum"})

        facture = {
            "Company_title" : a0.text,
            "Company_url" : company_url,
            "Recruit_title" : a1.text,
            "Recruit_url" : recruit_url,
            "Careers" : spans[0].text,
            "Position" : spans[2].text,
            "Deadline" : span.text
        }
        #print(json.dumps(facture, ensure_ascii=False))
        datas.append(facture)
        #print("========================================================================")
    return datas

def Parse_Job(URL):
    newcomers = {
        1:[], #1            웹프로그래머
        2:[], #2    응용프로그래머
        3:[], #3         시스템 프로그래머
        4:[], #4       DBA 데이터베이스
        5:[], #5        네트워크, 서버, 보안
        6:[], #6        웹기획 PM
        7:[], #7      웹마케팅
        8:[], #8       컨텐츠, 사이드운영
        9:[], #9         HTML, 퍼블리싱, UI개발
        10:[], #10     웹디자인
        11:[], #11        QA테스터, 검증
        12:[], #12          게임
        13:[], #13           ERP, 시스템 설계 및 분석
        14:[], #14       IT, 디자인, 컴퓨터 강사
        15:[], #15         동영상제작, 편집
        16:[], #16    빅데이터, 인공지능(AI)
        17:[], #17         소프트웨어 하드웨어
    }


    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('http://www.jobkorea.co.kr/recruit/joblist?menucode=duty')
    #경력 선택
    career_btn = whiledriver(driver, '//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[3]/dt')
    if(career_btn == False):
        driver.quit()
        return False
    else:
        career_btn.click()
    
    #신입 선택
    driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[3]/dd/div[1]/ul[1]/li[1]/label').click()
    #학력 선택
    driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[4]/dt').click()
    #고졸 선택
    driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[4]/dd/div[1]/ul/li[5]/label/span/span').click()
    #직무 버튼 선택
    driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dt').click()
    #//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dt/p
    #driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[4]/dd/div[1]/ul/li[6]/label').click()

    JOBCNT = 1
    while(JOBCNT <= 17):
        if(JOBCNT > 1):
            driver.find_element_by_xpath('//*[@id="toolitems"]/li[@class="duty item"]/button').click()

        #IT, Internet 버튼 선택
        driver.find_element_by_xpath('//*[@id="devSearchForm"]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[3]/label').click()
        #직종 선택 1~17
        driver.find_element_by_xpath('//*[@id="duty_step2_10016_ly"]/li['+str(JOBCNT)+']').click()
        #조건 검색하기
        driver.find_element_by_xpath('//*[@id="dev-btn-search"]').click()
        sleep(3)
        
        len_page = PageLength(driver)
        next_page = len_page // 400
        len_page = len_page // 40 + 1
        #LIS BTN : //*[@id="dvGIPaging"]/div/ul/li[1]
        #NEXT BTN : //*[@id="dvGIPaging"]/div/p/a

        BtnNext = 0
        res = []
        while(BtnNext <=next_page):
            if(BtnNext > 0):
                driver.find_element_by_xpath('//*[@id="dvGIPaging"]/div/p/a').click()
                sleep(1)
            if len_page // 10 == 0:
                ifs = len_page%10
            else:
                ifs = 10
            for lnt in range(1,ifs+1):
                if(lnt > 1):
                    driver.find_element_by_xpath('//*[@id="dvGIPaging"]/div/ul/li['+str(lnt)+']').click()
                    sleep(0.5)
                res = parse_data(driver, res)
            len_page -= 10
            BtnNext += 1
        newcomers[JOBCNT] = res
        JOBCNT += 1
    
    driver.quit()
    return newcomers