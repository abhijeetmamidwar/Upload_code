# MAJOR INSTRUCTIONS TO BE FOLLOWED BEFORE USING THIS PROJECT
# CHANGE CHROME DRIVER PATH ( ENTER YOUR OWN PATH ) ( i.e. chrome_driver_path )
# CREATE TWO FOLDERS NAMED " Fully_solved_codechef"   AND   " Partially_solved_codechef"
# CHANGE USERNAME FOR CODECHEF ( i.e. USERNAME )
# THIS FILE MUST BE RUN ONLY WHEN YOU HAVE USED IT BEFORE


import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# USERNAME = "abhijeet_1411"
USERNAME = "abhimamidwar"

chrome_driver_path = r"C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# edge_driver_path = r"C:\Users\abhijeet\Documents\Python Scripts\Projects\Github_code_uploader\msedgedriver.exe"
# driver = webdriver.Edge(executable_path=edge_driver_path)

driver.maximize_window()

link1 = "https://www.codechef.com/contests?itm_medium=navmenu&itm_campaign=allcontests"

# THIS IS THE MAIN LINK USED
link2 = f"https://www.codechef.com/users/{USERNAME}"

driver.get(link2)

# # Login Done
# driver.find_element_by_class_name("form-text").send_keys("abhijeet_1411")
# driver.find_element_by_name("pass").send_keys("Code14_11abhi")
# driver.find_element_by_id("edit-submit").click()
#
# # Go to Profile
# driver.find_element_by_class_name("fa-caret-down").click()
# driver.find_element_by_xpath('//*[@id="custom-login"]/li[1]/span[2]/ul/li[1]').click()
#
# # Logout Done
# driver.find_element_by_id("logout-btn").click()


"""  Fully solved """

f = open("fully.json", "r")
data = json.load(f)
f.close()

fully_solved_ids_with_questionCode = data
i = 1  # TRAVERSING ON EVERY CONTEST WHICH HAS PARTIAL SOLUTION SUBMITTED
while True:

    try:
        #  TRAVERSING THROUGH EVERY CONTEST
        P = driver.find_element_by_xpath(f'/html/body/main/div/div/div/div/div/section[5]/div/article[1]/p[{i}]')

        # EXTRACTING TEXT AND SPLITTING
        T = P.text.split(":")
        SP = T[1].split(",")

        j = 1  # INITIALIZING 'J' FOR TRAVERSING EVERY QUESTION SOLVED IN RESPECTIVE CONTEST
        while True:
            try:
                # GO THROUGH EACH AND EVERY QUESTION SOLVED IN CONTEST
                E = driver.find_element_by_xpath(
                    f"/html/body/main/div/div/div/div/div/section[5]/div/article[1]/p[{i}]/span/a[{j}]")

                question_code = E.text

                if question_code not in fully_solved_ids_with_questionCode:

                    # CLICK ON EVERY LINK IN PARTICULAR CONTEST
                    E.send_keys(Keys.ENTER)

                    # VERDICT OF ANSWER ( TRUE OR FALSE )

                    k = 1  # INITIALIZING 'K' FOR TRAVERSING IN ALL SUBMISSIONS FOR GIVEN QUESTION
                    while True:
                        try:

                            # CHECK IMAGE WERE IT IS CORRECT , PARTIALLY CORRECT OR FULLY CORRECT
                            Img = driver.find_element_by_xpath(
                                f'//*[@id="content"]/div/div/div[3]/table/tbody/tr[{k}]/td[4]/span/img')

                            # IF IT IS NOT WRONG ANSWER
                            if Img.get_attribute('src') == "https://cdn.codechef.com/misc/tick-icon.gif":

                                # GET SOLUTION NUMBER
                                solution_number = driver.find_element_by_xpath(
                                    f'//*[@id="content"]/div/div/div[3]/table/tbody/tr[{k}]/td[1]').text

                                fully_solved_ids_with_questionCode[question_code] = solution_number
                                # fully_solved_ids_with_questionCode[T[0]].append({question_code: solution_number})
                                break
                            else:
                                # IF TOP MOST SUBMISSION NOT PARTIALLY OR FULLY CORRECT INCREMENT 'K' BY 1
                                k += 1
                        except:
                            break

                    # GETTING BACK TO USER PROFILE PAGE
                    driver.back()

                # SWITCHING TO NEXT QUESTION BY INCREMENTING 'J' BY 1
                j += 1

            except:
                break

        # SWITCHING TO NEXT CONTEST BY INCREMENTING 'I' BY 1
        i += 1

    except:
        break

f = open("ftemp.json", "w")
f.write(json.dumps(fully_solved_ids_with_questionCode))
f.close()

"""  Partially solved """

f = open("partially.json", "r")
data = json.load(f)
f.close()

partially_solved_ids_with_questionCode = data
i = 1  # TRAVERSING ON EVERY CONTEST WHICH HAS PARTIAL SOLUTION SUBMITTED
while True:

    try:
        #  TRAVERSING THROUGH EVERY CONTEST
        P = driver.find_element_by_xpath(f'/html/body/main/div/div/div/div/div/section[5]/div/article[2]/p[{i}]')

        # EXTRACTING TEXT AND SPLITTING
        T = P.text.split(":")
        SP = T[1].split(",")

        j = 1  # INITIALIZING 'J' FOR TRAVERSING EVERY QUESTION SOLVED IN RESPECTIVE CONTEST
        while True:
            try:
                # GO THROUGH EACH AND EVERY QUESTION SOLVED IN CONTEST
                E = driver.find_element_by_xpath(
                    f"/html/body/main/div/div/div/div/div/section[5]/div/article[2]/p[{i}]/span/a[{j}]")

                # QUESTION CODE
                question_code = E.text

                if question_code not in partially_solved_ids_with_questionCode:

                    # CLICK ON EVERY LINK IN PARTICULAR CONTEST IF IT IS NOT PRESENT ALREADY
                    E.send_keys(Keys.ENTER)

                    # VERDICT OF ANSWER ( TRUE OR FALSE )

                    k = 1  # INITIALIZING 'K' FOR TRAVERSING IN ALL SUBMISSIONS FOR GIVEN QUESTION
                    while True:
                        try:

                            # CHECK IMAGE WERE IT IS CORRECT , PARTIALLY CORRECT OR FULLY CORRECT
                            Img = driver.find_element_by_xpath(
                                f'//*[@id="content"]/div/div/div[3]/table/tbody/tr[{k}]/td[4]/span/img')

                            # IF IT IS NOT WRONG ANSWER
                            if Img.get_attribute('src') != "https://cdn.codechef.com/misc/cross-icon.gif":

                                # GET SOLUTION NUMBER
                                solution_number = driver.find_element_by_xpath(
                                    f'//*[@id="content"]/div/div/div[3]/table/tbody/tr[{k}]/td[1]').text

                                partially_solved_ids_with_questionCode[question_code] = solution_number
                                # partially_solved_ids_with_questionCode[T[0]].append({question_code: solution_number})
                                break
                            else:
                                # IF TOP MOST SUBMISSION NOT PARTIALLY OR FULLY CORRECT INCREMENT 'K' BY 1
                                k += 1
                        except:
                            break

                    # GETTING BACK TO USER PROFILE PAGE
                    driver.back()

                # SWITCHING TO NEXT QUESTION BY INCREMENTING 'J' BY 1
                j += 1

            except:
                break

        # SWITCHING TO NEXT CONTEST BY INCREMENTING 'I' BY 1
        i += 1

    except:
        break

f = open("ptemp.json", "w")
f.write(json.dumps(partially_solved_ids_with_questionCode))
f.close()

driver.close()
