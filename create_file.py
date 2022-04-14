# CHANGE USERNAME HERE TO AND DONE
# RUN THE FILE
# OUTPUT OF THIS PROJECT GIVES YOU TWO FOLDERS NAMED "Fully_solved_codechef_{USERNAME}" AND "Partially_solved_codechef_{USERNAME}"
# THESE OTH FOLDER CONSISTS OF YOUR RESPECTIVE SOLVED QUESTIONS ON CODECHEF


import json
import pyperclip
from selenium import webdriver

# USERNAME = "abhijeet_1411"
USERNAME = "abhimamidwar"

chrome_driver_path = r"C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# edge_driver_path = r"C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\msedgedriver.exe"
# driver = webdriver.Edge(executable_path=edge_driver_path)

driver.maximize_window()


# FULLY SOLVED QUESTIONS
f = open("Fully.json", "r")
data = json.load(f)
f.close()

path_for_fully = f'C:/Users/abhijeet/Documents/Python Scripts/Github_code_uploader/Fully_solved_codechef'

for i in data:
    driver.get(f"https://www.codechef.com/viewsolution/{data[i]}")
    try:
        copy_button = driver.find_element_by_id('copy-button').click()
        Code = pyperclip.paste()
        file = open(f'{path_for_fully}\{i}.txt', 'w')
        file.write(Code)
        file.close()
    except:
        break


# PARTIALLY SOLVED QUESTIONS
f = open("partially.json", "r")
data = json.load(f)
f.close()

path_for_partially = f'C:/Users/abhijeet/Documents/Python Scripts/Github_code_uploader/Partially_solved_codechef'

for i in data:
    driver.get(f"https://www.codechef.com/viewsolution/{data[i]}")
    try:
        copy_button = driver.find_element_by_id('copy-button').click()
        Code = pyperclip.paste()
        file = open(f'{path_for_partially}\{i}.txt', 'w')
        file.write(Code)
        file.close()
    except:
        break

driver.close()
