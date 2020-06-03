# from selenium import webdriver 
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate

driver = webdriver.Firefox(executable_path =r'C:\Users\JasonPC\geckodriver-v0.26.0-win64\geckodriver.exe')
# driver.implicitly_wait(120) # https://selenium-python.readthedocs.io/waits.html
driver.get('https://sjc.linways.com/student/')
# headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/72.0.2'}
# req = requests.get(url, headers = headers)

username = driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[2]/div/input[1]")
username.send_keys('18BCA41002')
time.sleep(7)
password = driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[2]/div/input[2]")
password.send_keys("18BCA41002")
submit_btn = driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/div[2]/div/a/button/span[2]")
submit_btn.click()

time.sleep(20) # sleeps for 20 seconds

email = driver.find_element_by_xpath("//*[@id='identifierId']")
email.send_keys("xxxxxxxxxx@gmail.com") # email
time.sleep(20)
email_next_btn1 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span")
email_next_btn1.click()

time.sleep(20) # sleeps for 10 seconds

email_pass = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
email_pass.send_keys("xxxxxxxxx") # password
time.sleep(20)
email_next_btn2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span")
email_next_btn2.click()

time.sleep(30)

attendance_tab = driver.find_element_by_id("studentattendance")
attendance_tab.click()

time.sleep(20) # time given for the attedance data to load

# heading = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/b")
# print(heading)

'''
attendance_panel = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]")
attendance_panel = str(attendance_panel.text) #convert it to string type
delimiter = "\\n"
print(attendance_panel.split(delimiter))
'''

# variables containing data of number of hours attended od each subject
gen_eng = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[1]/td[3]")
add_eng = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[2]/td[3]")
java_lab = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[3]/td[3]")
envt = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[4]/td[3]")
market = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[5]/td[3]")
java = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[6]/td[3]")
unix = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[7]/td[3]")
networks = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[8]/td[3]")
unix_lab = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[9]/td[3]")

time.sleep(2)

# variables containing data total number of hours of subject
gen_eng_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[1]/td[4]")
add_eng_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[2]/td[4]")
java_lab_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[3]/td[4]")
envt_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[4]/td[4]")
market_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[5]/td[4]")
java_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[6]/td[4]")
unix_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[7]/td[4]")
networks_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[8]/td[4]")
unix_lab_tot = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[9]/td[4]")

time.sleep(2)

# varibales containing data of total percentage of the attendance of each subject
gen_eng_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[1]/td[5]")
add_eng_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[2]/td[5]")
java_lab_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[3]/td[5]")
envt_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[4]/td[5]")
market_perc =  driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[5]/td[5]")
java_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[6]/td[5]")
unix_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[7]/td[5]")
networks_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[8]/td[5]")
unix_lab_perc = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody[1]/tr[9]/td[5]")

print('---------------------------------------------Jason\'s Attendance---------------------------------------------')

headers = ["Sl No", "Subject Name", "Number of Attended Hour", "Total Hour", "Attedance Percentage", "Attedance Percentage in Class"]
table = [[1, "General English", gen_eng.text, gen_eng_tot.text, gen_eng_perc.text], 
		 [2, "Additional English" , add_eng.text, add_eng_tot.text, add_eng_perc.text],
		 [3, "Java Lab", java_lab.text, java_lab_tot.text, java_lab_perc.text],
		 [4, "Environment and Health", envt.text, envt_tot.text, envt_perc.text],
		 [5, "Marketing Management", market.text, market_tot.text, market_perc.text],
		 [6, "Java Programming", java.text, java_tot.text, java_perc.text],
		 [7, "Unix Programming", unix.text, unix_tot.text, unix_perc.text],
		 [8, "Computer Networks", networks.text, networks_tot.text, networks_perc.text],
		 [9, "Unix Lab", unix_lab.text, unix_lab_tot.text, unix_lab_perc.text]]

print(tabulate(table, headers, tablefmt="fancy_grid")) # prints the final attendance table
