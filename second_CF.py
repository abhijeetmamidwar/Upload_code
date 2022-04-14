##### CREATE FILE APP FOR SECOND PY FILE
# RUN THIS CODE WHEN second.py file is run already
# AFTER RUNNING THIS FILE UPLOAD ALL FILES IN temp_fully and temp_partially TO GITHUB AND DELETE ALL FILES IN THEM
# CHANGE CHROME DRIVER PATH ( ENTER YOUR OWN PATH ) ( i.e. chrome_driver_path )
# CREATE TWO FOLDERS NAMED " Fully_solved_codechef"   AND   " Partially_solved_codechef"
# CHANGE USERNAME FOR CODECHEF ( i.e. USERNAME )
# FIRST EXECUTE main.py THEN EXECUTE create_file.py

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
f = open("fully.json", "r")
previous_data_fully = json.load(f)
f.close()

f = open("ftemp.json","r")
current_data_fully = json.load(f)
f.close()

path_for_fully = r'C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\temp_fully'

for i in current_data_fully:
    if i not in previous_data_fully:
        driver.get(f"https://www.codechef.com/viewsolution/{current_data_fully[i]}")
        try:
            copy_button = driver.find_element_by_id('copy-button').click()
            Code = pyperclip.paste()
            file = open(f'{path_for_fully}\{i}.txt', 'w')
            file.write(Code)
            file.close()
        except:
            break

f = open("fully.json","a")
f.write(json.dumps(current_data_fully))
f.close()


# PARTIALLY SOLVED QUESTIONS
f = open("partially.json", "r")
previous_data_partially = json.load(f)
f.close()

f = open("ptemp.json","r")
current_data_partially = json.load(f)
f.close()

path_for_partially = r'C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\temp_partially'

for i in current_data_partially:
    if i not in previous_data_partially:
        driver.get(f"https://www.codechef.com/viewsolution/{current_data_partially[i]}")
        try:
            copy_button = driver.find_element_by_id('copy-button').click()
            Code = pyperclip.paste()
            file = open(f'{path_for_partially}\{i}.txt', 'w')
            file.write(Code)
            file.close()
        except:
            break

driver.close()

f = open("partially.json","a")
f.write(json.dumps(current_data_partially))
f.close()