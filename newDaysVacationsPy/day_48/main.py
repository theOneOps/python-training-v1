from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = "C:/Users/medew/OneDrive\Bureau/automationPython/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=f"{chrome_driver}")
driver.get("https://www.python.org/")
all_events = driver.find_elements(By.CSS_SELECTOR, ".menu li time+a")
all_times = driver.find_elements(By.CSS_SELECTOR, ".menu li time")
for i in all_events[5:]:
    print(i.text)

for i in all_times[5:]:
    print(i.text)

thedictOne = {value.text: name.text for name in all_events[5:] for value in all_times[5:]}
theList = {i: event for i in range(len(thedictOne)+1) for event in [{key: thedictOne.get(key)} for key in thedictOne.keys() for item in thedictOne.items()]}
print(theList)
driver.quit()


