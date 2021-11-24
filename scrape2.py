import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# Create list of TopLEvelDomain from CSV file
tdl_list =[]
with open('TLD_List.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        tdl_list.append(line[0])

# gives the path of my chromiumdriver
PATH = '/usr/local/bin/chromedriver/chromedriver'
driver = webdriver.Chrome(PATH)
driver.set_page_load_timeout(20)

for tld in tdl_list:
    address = 'http://www.renzo'+tld

    try:
        driver.get(address)
        print(address, " = ", driver.title)
        driver.get_screenshot_as_png()

    except TimeoutException as ex:
        print(address, " = **** TIMEOUT")

    except:
        print(address, " = Nothing")


