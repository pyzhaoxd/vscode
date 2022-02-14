from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
prefs = {"profile.default_content_setting_values.automatic_downloads": 1,
         #"download.default_directory": "/home/shaohua/PycharmProjects/Python/download"
         }
chrome_options.add_experimental_option('prefs', prefs)
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# try:
browser.get('https://sdwanr2.ctclouds.com/versa/login')
input_username = browser.find_element_by_id('inputEmail')
input_username.send_keys('ZhaoXiaoDong')
input_pwd = browser.find_element_by_id('inputPassword')
input_pwd.send_keys('Zhaoxd@4321')
click_button = browser.find_element_by_name('submit-button')
click_button.click()
browser.implicitly_wait(60)

#     click_template = browser.find_element_by_xpath('//*[@id="menuContainer"]/li[2]/a')
#     click_template.click()
#     for line in open('hub_list.txt'):
#         input_search = browser.find_element_by_xpath('//*[@id="object-listing-actions"]/div[2]/ul/li/input')
#         input_search.send_keys(line)
#         input_search.send_keys(Keys.ENTER)
#         select_template = browser.find_element_by_xpath(
#             '/html/body/div[2]/div[1]/div/div[4]/div[3]/div[1]/div[1]/div[3]/div/div'
#             '/div/div/div[3]/div[3]/div/div/div/table/tbody/tr[2]/td[1]/div/input')
#         select_template.click()
#         export_template = browser.find_element_by_xpath(
#             '//*[@id="object-listing-actions"]/div[3]/div/div/ul/li[5]/span')
#         export_template.click()
#         clear_search = browser.find_element_by_xpath('//*[@id="object-listing-actions"]/div[2]/ul/li/input')
#         clear_search.clear()
#         browser.implicitly_wait(3)
#         time.sleep(1)

# finally:
#     print("all cfg files export completed")
#     time.sleep(3)
#     #browser.close()