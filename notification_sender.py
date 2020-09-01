from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
import smtplib
import time

current_date = date.today()
current_date = str(current_date.strftime("%d.%m.%Y"))

op = webdriver.ChromeOptions()
op.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver',options=op)
driver.get('///')

#latest = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div[8]/div[1]/ul/li[1]/time')
latest2 = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[8]/div[1]/ul/li[1]/time')
#latest = driver.find_elements_by_xpath("//*[contains(text(), '01.09.2020')]")
if latest2[0].text == current_date:
	element = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[8]/div[1]/ul/li[1]/a')
	href = element[0].get_attribute('href')
	txt_subj = element[0].text

	user = "///"
	pas = "///"

	body = """Subject: New post from FMI 

	Post date: {}
	Post subject: {}
	Link: {}

	All the best, 
		You from the past.

	""".format(latest2[0].text, txt_subj, href)

	s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
	s.login(user, pas)
	s.sendmail(user, user, body.encode('utf-8'))
	# s.quit()

else:
	print('No new updates')

time.sleep(2)

driver.close()
quit()

