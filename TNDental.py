import time
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver,5)
    return driver

workbook = xlsxwriter.Workbook('TNDental.xlsx')
worksheet = workbook.add_worksheet()
row = 0

driver = init_driver()
driver.get("http://www.tndentalcouncil.org/Account/RegisteredDentist")
time.sleep(2)

for counter in range(1,1325):

    button_next = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnNext")))
    for counter_page in range(2,17):
        if counter_page < 10 :
            num = "0"+str(counter_page)
        else:
            num = str(counter_page)

        Code_id = "gdvLstregDentist_ctl"+num+"_Label_code"
        RegDate_id = "gdvLstregDentist_ctl"+num+"_Label_regdate"
        Name_id = "gdvLstregDentist_ctl"+num+"_Label_name"
        Qual_id = "gdvLstregDentist_ctl"+num+"_Label_qual"
        Val_id = "gdvLstregDentist_ctl"+num+"_Label_val"
        Addr_id = "gdvLstregDentist_ctl"+num+"_Label_addr"

        Code = driver.find_element_by_id(Code_id).text
        RegDate = driver.find_element_by_id(RegDate_id).text
        Name = driver.find_element_by_id(Name_id).text
        Qual = driver.find_element_by_id(Qual_id).text
        Val = driver.find_element_by_id(Val_id).text
        Addr = driver.find_element_by_id(Addr_id).text

        worksheet.write(row, 0, Code)
        worksheet.write(row, 1, RegDate)
        worksheet.write(row, 2, Name)
        worksheet.write(row, 3, Qual)
        worksheet.write(row, 4, Val)
        worksheet.write(row, 5, Addr)

        row = row + 1
        print("{} {} {} {}".format(row, Code, Name, Qual))
        counter_page = counter_page + 1

    button_next = driver.wait.until(EC.element_to_be_clickable((By.NAME, "btnNext")))
    button_next.click()
    #print(counter)
    counter = counter + 1
workbook.close()
driver.quit()
