from anticaptchaofficial.imagecaptcha import imagecaptcha
# from captcha.image import ImageCaptcha
from selenium import webdriver
import string
import random

from selenium.webdriver.common.keys import Keys

import  mail_generator
# from pygame import mixer
import time
from nordvpn_switcher import initialize_VPN,rotate_VPN

# mixer.init()
# mixer.music.load('sound.mp3')


def main_sele(email, loc, fName, lName, DoB, pNo, p_issue_date, p_exp_date, p_place, email_df, instructions):

    while True:
        try:
            rotate_VPN(instructions)  # refer to the instructions variable here

            driver = webdriver.Chrome('chromedriver.exe')
            driver.maximize_window()
            driver.get('https://morocco.blsspainvisa.com/english/register.php')
            time.sleep(1) # Let the user actually see something!

            # Set Name
            name_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[1]/div[2]/input')
            break
        except:
            driver.close()
    name_box.click()
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    name_box.send_keys(name)

    # Set Email
    email_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[2]/div[2]/input')
    email_box.click()
    email_box.send_keys(email)

    # Set Phone
    rand_numbers = string.digits
    phone = ''.join(random.choice(rand_numbers) for i in range(8))

    phone = '7' + phone
    phone_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[3]/div[2]/div[2]/input')
    phone_box.click()
    phone_box.send_keys(phone)

    # Set Location
    location_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[4]/div[2]/select')
    location_box.click()
    locations_list = ['/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[2]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[3]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[4]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[5]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[6]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[7]']
    location = random.choice(locations_list)
    location_selection = driver.find_element_by_xpath(location)
    location_selection.click()

    captcha_img = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[5]/div/div[1]/img')
    driver.execute_script("window.scrollTo(0, 150)")
    captcha_img.screenshot('captcha_img.png')
    # c45e8d9fa99fdc3beb5ed2087359f1fe

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("40614f72b7eebc50f8512784279dde15")

    text = solver.solve_and_return_solution("captcha_img.png")
    if text != 0:
        print("captcha text " + text)
    else:
        print("task finished with error " + solver.error_code)
        refresh = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[5]/div/div[2]/a')
        refresh.click()

    # Set Captcha
    captcha_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[6]/div[2]/input')
    captcha_box.clear()
    captcha_box.click()
    captcha_box.send_keys(text)

    captcha_box.send_keys(Keys.BACK_SPACE)
    captcha_box.send_keys(text[-1])
    time.sleep(1)

    # Press Register
    register = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[7]/input')
    register.click()
    time.sleep(2)

    # Activate
    activation, password, otp, verfiy_code = mail_generator.checkMails()
    driver.get(activation)
    time.sleep(1)

    driver.get('https://morocco.blsspainvisa.com/english/login.php')
    email_login = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div[1]/div[1]/div[2]/input')
    email_login.send_keys(email)
    time.sleep(2)

    continue_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div[1]/div[2]')
    continue_box.click()
    time.sleep(2)



    # Find OTP:
    activation, password1, otp, verfiy_code = mail_generator.checkMails()

    # Send OTP and Password
    otp_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[1]/div[2]/input')
    otp_box.send_keys(otp)

    password_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[2]/div[2]/input')
    password_box.send_keys(password)

    # Press Login:
    login_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[3]')
    time.sleep(2)
    login_box.click()
    time.sleep(1)

    # Close button:
    close_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close_button.click()

    # Fill Page 2:
    driver.execute_script("window.scrollTo(0, 1000)")

    # Choose Center
    centre_button = driver.find_element_by_xpath(
        '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select')
    centre_list = ['/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[2]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[3]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[4]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[5]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[6]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[7]']

    #centre = random.choice(centre_list)
    centre_selection = driver.find_element_by_xpath(centre_list[loc - 1])
    centre_selection.click()
    time.sleep(1)
    # Close: Cl
    close_list = ['/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[6]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[5]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[4]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[3]/div/div[1]']

    close_1 = driver.find_element_by_xpath(close_list[loc - 1])
    close_1.click()

    # Travel Date:
    if centre_selection.text == 'Casablanca':
        travel_date_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')
        travel_date_box.click()

        travel_date = '2022-Apr-25'
        year = travel_date[0:4]
        month = travel_date[5:8]
        day = travel_date[9:11].lstrip('0')


        next_button = driver.find_element_by_xpath('/html/body/div[9]/div[3]/table/thead/tr/th[3]')

        # Year:
        i = 1
        while True:
            sel_year = driver.find_element_by_xpath('/html/body/div[9]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_year.text == year:
                sel_year.click()
                break

            if i == 12:
                next_button.click()
                i = 0
            i = i + 1

        # Month:
        i = 1
        while i <= 12:
            sel_month = driver.find_element_by_xpath('/html/body/div[9]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_month.text == month:
                sel_month.click()
                break
            i = i + 1

        # Day:
        check = 0
        check_day_one = 0
        for i in range(6):
            if not check:
                for j in range(7):
                    day_sel = driver.find_element_by_xpath(
                        '/html/body/div[9]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                    if not check_day_one and int(day_sel.text) != 1:
                        continue
                    else:
                        check_day_one = True
                    if day_sel.text == day and check_day_one:
                        check = 1
                        day_sel.click()
                        break

        # Shengen:
        shengen_box_no = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/select/option[2]')
        shengen_box_yes = driver.find_element_by_xpath(
            '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/select/option[3]')
        shengen_box_no.click()

        #Close
        try:
            close_4 = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]')
            close_4.click()
        except:
            pass

    # Category:
    appli_cate = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[5]/div[2]/select/option[2]')
    appli_cate.click()


    # Verification:
    req_veri = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[8]/div[2]/abbr/input')
    req_veri.click()

    # Close 2:
    close_2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close_2.click()
    time.sleep(1)

    activation, password1, otp, verfiy_code = mail_generator.checkMails()

    verify_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[9]/div[2]/input[1]')
    verify_box.send_keys(verfiy_code)
    time.sleep(1)
    verify_box.click()

    # Next Page:
    continue2_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[9]/div[3]/input')
    continue2_box.click()

    # Close3:
    close3 = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close3.click()

    driver.execute_script("window.scrollTo(0, 3000)")


    agree_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div/div[3]/div[1]/button')
    agree_box.click()

    # Date Selection:
    check = 0
    x = 0
    while not check:
        if x == 1:
            time.sleep(8)
        driver.get('https://morocco.blsspainvisa.com/english/appointment.php')
        x = 1
        try:
            date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input')
            
            date_box.click()
            
            time.sleep(1)
            try:
                next_button = driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/thead/tr[1]/th[3]')
                next_button.click()
            except:
                pass


            check = 0
            for i in range(5, -1, -1):
                if not check:
                    for j in range(6, -1, -1):
                        date = driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/tbody/tr[' + str(i+1) + ']/td[' + str(j+1) + ']')
                        if date.get_attribute('title') == 'Book':
                            # mixer.music.play()

                            check = 1
                            date.click()

                            break
                else:
                    break


        except:
            time.sleep(8)
            driver.get('https://morocco.blsspainvisa.com/english/appointment.php')
    final_Date = driver.find_element_by_xpath(
        '/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/input')
    selected_date = final_Date.get_attribute('value')

    # Time
    while True:
        try:
            time_app = driver.find_element_by_xpath(
                '/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/select/option[2]')
            time_app.click()
            break
        except:
            print('Time error')
            time.sleep(2)

    selected_time = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/select')
    selected_time = selected_time.get_attribute('value')
    # Visa:
    visa = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[8]/td[2]/select/option[2]')
    visa.click()

    # Name
    f_name = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[9]/td[2]/input')
    f_name.send_keys(fName)
    l_name = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/input')
    l_name.send_keys(lName)

    # DoB:
    userDoB = DoB
    year = userDoB[0:4]
    month = userDoB[5:8]
    day = userDoB[9:11].lstrip('0')

    DoB = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/input')
    DoB.click()

    back_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[1]')

    # Year:
    i = 1
    while True:
        sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_year.text == year:
            sel_year.click()
            break

        if i == 12:
            back_button.click()
            i = 0
        i = i + 1

    # Month:
    i = 1
    while i <= 12:
        sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_month.text == month:
            sel_month.click()
            break
        i = i + 1

    # Day
    check = 0
    check_day_one = 0
    for i in range(6):
        if not check:
            for j in range(7):
                day_sel = driver.find_element_by_xpath(
                    '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')

                if not check_day_one and int(day_sel.text) != 1:
                    continue
                else:
                    check_day_one = True
                if day_sel.text == day and check_day_one:
                    check = 1
                    day_sel.click()
                    break




    # Passport Num:
    passport_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[15]/td[2]/input')
    passport_box.send_keys(pNo)
    driver.execute_script("window.scrollTo(0, 500)")
    # Issue Date:
    issue_date = p_issue_date
    year = issue_date[0:4]
    month = issue_date[5:8]
    day = issue_date[9:11].lstrip('0')
    issue_date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[16]/td[2]/input')
    issue_date_box.click()

    back_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[1]')

    # Year:
    i = 1
    while True:
        sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_year.text == year:
            sel_year.click()
            break

        if i == 12:
            back_button.click()
            i = 0
        i = i + 1

    # Month:
    i = 1
    while i <= 12:
        sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_month.text == month:
            sel_month.click()
            break
        i = i + 1

    # Day
    check = 0
    check_day_one = 0
    for i in range(6):
        if not check:
            for j in range(7):
                day_sel = driver.find_element_by_xpath(
                    '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                if not check_day_one and int(day_sel.text) != 1:
                    continue
                else:
                    check_day_one = True
                if day_sel.text == day and check_day_one:
                    check = 1
                    day_sel.click()
                    break


    # Expiry Date:
    expiry_date = p_exp_date
    year = expiry_date[0:4]
    month = expiry_date[5:8]
    day = expiry_date[9:11].lstrip('0')
    expiry_date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[17]/td[2]/input')
    expiry_date_box.click()

    next_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[3]')

    # Year:
    i = 1
    while True:
        sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_year.text == year:
            sel_year.click()
            break

        if i == 12:
            next_button.click()
            i = 0
        i = i + 1

    # Month:
    i = 1
    while i <= 12:
        sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
        if sel_month.text == month:
            sel_month.click()
            break
        i = i + 1

    check = 0
    for i in range(6):
        if not check:
            for j in range(7):
                day_sel = driver.find_element_by_xpath(
                    '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                if day_sel.text == day:
                    check = 1
                    day_sel.click()
                    break

    # Issue Country:
    issue_country = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[18]/td[2]/input')
    issue_country.send_keys(p_place)
    email_df = email_df.append(
        {'Passport': pNo, 'Last Name': lName, 'First Name': fName, 'Email': email, 'Phone': phone, 'Date': selected_date,
         'Time': selected_time}, ignore_index=1)


    # Submit:
    while True:
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            submit_button = driver.find_element_by_xpath(
                '/html/body/div[1]/section[1]/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[23]/td[2]/input[7]')
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 700)")
            submit_button.click()
            time.sleep(1)
            alert_obj = driver.switch_to.alert
            time.sleep(2)
            alert_obj.accept()
            time.sleep(3)
            appoint = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div[2]')
            appoint.screenshot(lName + '_' + fName + '_Appointment.png')
            print('Done')
            break
        except:
            continue

    #appoint = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div[2]')
    #time.sleep(1)
    #driver.get_screenshot_as_file(lName + '_' + fName + '_Appointment.png')
    print('Done')
    return email_df


########################################################################################################################
################################################ FAMILY ################################################################
########################################################################################################################

def main_sele_family(email, loc, fName, lName, DoB, pNo, p_issue_date, p_exp_date, p_place, num, email_df, instructions):
    while True:
        try:
            # rotate_VPN(instructions)  # refer to the instructions variable here

            driver = webdriver.Chrome('chromedriver.exe')
            driver.maximize_window()
            driver.get('https://morocco.blsspainvisa.com/english/register.php')
            time.sleep(1) # Let the user actually see something!

            # Set Name
            name_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[1]/div[2]/input')
            break
        except:
            driver.close()

    name_box.click()
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))
    name_box.send_keys(name)

    # Set Email
    email_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[2]/div[2]/input')
    email_box.click()
    email_box.send_keys(email)

    # Set Phone
    rand_numbers = string.digits
    phone = ''.join(random.choice(rand_numbers) for i in range(8))
    phone = '7' + phone
    phone_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[3]/div[2]/div[2]/input')
    phone_box.click()
    phone_box.send_keys(phone)

    # Set Location
    location_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[4]/div[2]/select')
    location_box.click()
    locations_list = ['/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[2]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[3]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[4]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[5]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[6]',
                      '/html/body/div[1]/section/div/div/form/div[4]/div[2]/select/option[7]']
    location = random.choice(locations_list)
    location_selection = driver.find_element_by_xpath(location)
    location_selection.click()

    captcha_img = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[5]/div/div[1]/img')
    driver.execute_script("window.scrollTo(0, 150)")
    captcha_img.screenshot('captcha_img.png')

    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("40614f72b7eebc50f8512784279dde15")

    text = solver.solve_and_return_solution("captcha_img.png")
    if text != 0:
        print("captcha text " + text)
    else:
        print("task finished with error " + solver.error_code)
        refresh = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[5]/div/div[2]/a')
        refresh.click()

    print(text)

    # Set Captcha
    captcha_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[6]/div[2]/input')
    captcha_box.clear()
    captcha_box.click()
    captcha_box.send_keys(text)
    time.sleep(1)

    # Press Register
    register = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/form/div[7]/input')
    register.click()
    time.sleep(3)
    
    # Activate
    activation, password, otp, verfiy_code = mail_generator.checkMails()
    driver.get(activation)
    time.sleep(2)

    driver.get('https://morocco.blsspainvisa.com/english/login.php')
    email_login = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div[1]/div[1]/div[2]/input')
    email_login.send_keys(email)
    time.sleep(2)

    continue_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div[1]/div[2]')
    continue_box.click()
    time.sleep(2)

    # Find OTP:
    activation, password1, otp, verfiy_code = mail_generator.checkMails()

    # Send OTP and Password
    otp_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[1]/div[2]/input')
    otp_box.send_keys(otp)

    password_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[2]/div[2]/input')
    password_box.send_keys(password)

    # Press Login:
    login_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/form/div/div[3]')
    time.sleep(2)
    login_box.click()
    time.sleep(1)

    # Close button:
    close_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close_button.click()

    # Fill Page 2:
    driver.execute_script("window.scrollTo(0, 1000)")

    # Choose Family:
    family_button = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[1]/div[2]/div[3]/input')
    family_button.click()

    members = ['/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[1]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[2]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[3]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[4]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[5]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[6]',
               '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[2]/div[2]/select/option[7]']

    members_selection = driver.find_element_by_xpath(members[num - 2])
    members_selection.click()



    # Choose Center
    centre_button = driver.find_element_by_xpath(
        '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select')
    centre_list = ['/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[2]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[3]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[4]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[5]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[6]',
                      '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/select/option[7]']

    #centre = random.choice(centre_list)
    centre_selection = driver.find_element_by_xpath(centre_list[loc - 1])
    centre_selection.click()
    time.sleep(1)
    # Close: Cl
    close_list = ['/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[6]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[5]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[4]/div/div[1]',
                  '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[3]/div[2]/div[3]/div/div[1]']
    close_1 = driver.find_element_by_xpath(close_list[loc - 1])
    close_1.click()

    # Travel Date:
    if centre_selection.text == 'Casablanca':
        travel_date_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/input')
        travel_date_box.click()

        travel_date = '2022-Apr-25'
        year = travel_date[0:4]
        month = travel_date[5:8]
        day = travel_date[9:11].lstrip('0')


        next_button = driver.find_element_by_xpath('/html/body/div[9]/div[3]/table/thead/tr/th[3]')

        # Year:
        i = 1
        while True:
            sel_year = driver.find_element_by_xpath('/html/body/div[9]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_year.text == year:
                sel_year.click()
                break

            if i == 12:
                next_button.click()
                i = 0
            i = i + 1

        # Month:
        i = 1
        while i <= 12:
            sel_month = driver.find_element_by_xpath('/html/body/div[9]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_month.text == month:
                sel_month.click()
                break
            i = i + 1

        # Day:
        check = 0
        check_day_one = 0
        for i in range(7):
            if not check:
                for j in range(6):
                    day_sel = driver.find_element_by_xpath(
                        '/html/body/div[9]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                    if not check_day_one and int(day_sel.text) != 1:
                        continue
                    else:
                        check_day_one = True
                    if day_sel.text == day and check_day_one:
                        check = 1
                        day_sel.click()
                        break

        # Shengen:
        shengen_box_no = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/select/option[2]')
        shengen_box_yes = driver.find_element_by_xpath(
            '/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/select/option[3]')
        shengen_box_no.click()

        #Close
        try:
            close_4 = driver.find_element_by_xpath('/html/body/div[6]/div/div[1]')
            close_4.click()
        except:
            pass

    # Category:
    appli_cate = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[5]/div[2]/select/option[2]')
    appli_cate.click()


    # Verification:
    req_veri = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[8]/div[2]/abbr/input')
    req_veri.click()

    # Close 2:
    close_2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close_2.click()

    activation, password1, otp, verfiy_code = mail_generator.checkMails()

    verify_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[9]/div[2]/input[1]')
    verify_box.send_keys(verfiy_code)
    time.sleep(1)
    verify_box.click()

    # Next Page:
    continue2_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div[2]/div[2]/div[9]/div[3]/input')
    continue2_box.click()

    # Close3:
    close3 = driver.find_element_by_xpath('/html/body/div[1]/div[1]')
    close3.click()

    driver.execute_script("window.scrollTo(0, 3000)")


    agree_box = driver.find_element_by_xpath('/html/body/div[3]/form/section/div/div/div/div[3]/div[1]/button')
    agree_box.click()

    # Date Selection:
    check = 0
    x = 1
    while not check:
        try:
            if x == 0:
                time.sleep(7)
            x = 0
            driver.get('https://morocco.blsspainvisa.com/english/appointment_family.php')
            time.sleep(2)
            date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
            date_box.click()
            time.sleep(1)
            try:
                next_button = driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/thead/tr[1]/th[3]')
                next_button.click()
            except:
                pass
            check = 0
            for i in range(5, -1, -1):
                if not check:
                    for j in range(6, -1, -1):
                        date = driver.find_element_by_xpath('/html/body/div[8]/div[1]/table/tbody/tr[' + str(i+1) + ']/td[' + str(j+1) + ']')
                        if date.get_attribute('title') == 'Book':
                            # mixer.music.play()

                            check = 1
                            date.click()
                            break
                else:
                    break

            
        except:
            print('Error')
            driver.get('https://morocco.blsspainvisa.com/english/appointment_family.php')
            time.sleep(1)
    time.sleep(2)
    final_Date = driver.find_element_by_xpath(
        '/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input')

    selected_date = final_Date.get_attribute('value')
    kk = 2
    for cust in range(num):
        # Time
        try:
            time_app = driver.find_element_by_xpath(
                '/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[1]/td[1]/select/option['+ str(kk)+']')
            kk = kk + 1
        except:
            time_app = driver.find_element_by_xpath(
                '/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(
                    cust + 1) + ']/table/tbody/tr[1]/td[1]/select/option[' + str(kk-1) + ']')
            
        time_app.click()

        time.sleep(1)
        # Visa:
        visa = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[1]/td[2]/select/option[2]')
        visa.click()

        # Name
        f_name = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[1]/td[3]/input')
        f_name.send_keys(fName[cust])
        l_name = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[1]/td[4]/input')
        l_name.send_keys(lName[cust])
        l_name.click()
        # DoB:
        userDoB = DoB[cust]
        year = userDoB[0:4]
        month = userDoB[5:8]
        day = userDoB[9:11].lstrip('0')

        DoB_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[1]/td[5]/input')
        DoB_box.click()

        back_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[1]')

        # Year:
        i = 1
        while True:
            sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_year.text == year:
                sel_year.click()
                break

            if i == 12:
                back_button.click()
                i = 0
            i = i + 1

        # Month:
        i = 1
        while i <= 12:
            sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_month.text == month:
                sel_month.click()
                break
            i = i + 1

        # Day
        check = 0
        check_day_one = 0
        for i in range(6):
            if not check:
                for j in range(7):
                    day_sel = driver.find_element_by_xpath(
                        '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')

                    if not check_day_one and int(day_sel.text) != 1:
                        continue
                    else:
                        check_day_one = True
                    if day_sel.text == day and check_day_one:
                        check = 1
                        day_sel.click()
                        break




        # Passport Num:
        passport_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[2]/td[2]/input')
        passport_box.send_keys(pNo[cust])
        driver.execute_script("window.scrollTo(0, 300)")
        # Issue Date:
        issue_date = p_issue_date[cust]
        year = issue_date[0:4]
        month = issue_date[5:8]
        day = issue_date[9:11].lstrip('0')
        issue_date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[2]/td[3]/input')
        issue_date_box.click()

        back_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[1]')

        # Year:
        i = 1
        while True:
            sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_year.text == year:
                sel_year.click()
                break

            if i == 12:
                back_button.click()
                i = 0
            i = i + 1

        # Month:
        i = 1
        while i <= 12:
            sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_month.text == month:
                sel_month.click()
                break
            i = i + 1

        # Day
        check = 0
        check_day_one = 0
        for i in range(6):
            if not check:
                for j in range(7):
                    day_sel = driver.find_element_by_xpath(
                        '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                    if not check_day_one and int(day_sel.text) != 1:
                        continue
                    else:
                        check_day_one = True
                    if day_sel.text == day and check_day_one:
                        check = 1
                        day_sel.click()
                        break


        # Expiry Date:
        expiry_date = p_exp_date[cust]
        year = expiry_date[0:4]
        month = expiry_date[5:8]
        day = expiry_date[9:11].lstrip('0')
        expiry_date_box = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[2]/td[4]/input')
        expiry_date_box.click()

        next_button = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/thead/tr/th[3]')

        # Year:
        i = 1
        while True:
            sel_year = driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_year.text == year:
                sel_year.click()
                break

            if i == 12:
                next_button.click()
                i = 0
            i = i + 1

        # Month:
        i = 1
        while i <= 12:
            sel_month = driver.find_element_by_xpath('/html/body/div[8]/div[2]/table/tbody/tr/td/span[' + str(i) + ']')
            if sel_month.text == month:
                sel_month.click()
                break
            i = i + 1

        check = 0
        for i in range(6):
            if not check:
                for j in range(7):
                    day_sel = driver.find_element_by_xpath(
                        '/html/body/div[8]/div[1]/table/tbody/tr[' + str(i + 1) + ']/td[' + str(j + 1) + ']')
                    if day_sel.text == day:
                        check = 1
                        day_sel.click()
                        break

        # Issue Country:
        issue_country = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[8]/td/div/div[' + str(cust + 1) + ']/table/tbody/tr[2]/td[5]/input')
        issue_country.send_keys(p_place[cust])

        if cust == 0:
            final_time = time_app.get_attribute('value')
    # Submit:
    while True:
        try:
            driver.execute_script("window.scrollTo(0, 700)")
            submit_button = driver.find_element_by_xpath(
                '/html/body/div[1]/section[1]/div/div/div/form/table/tbody/tr/td/table/tbody/tr[14]/td[2]/input[7]')
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(int(num))
            driver.execute_script("window.scrollTo(0, 700)")
            submit_button.click()
            time.sleep(1)
            alert_obj = driver.switch_to.alert
            time.sleep(2)
            alert_obj.accept()
            time.sleep(3)
            #appoint = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div')
            #appoint.screenshot(lName + '_' + fName + '_Appointment.png')
            print('Done')
            break
        except:
            continue

    email_df = email_df.append(
        {'Passport': pNo, 'Last Name': lName, 'First Name': fName, 'Email': email, 'Phone': phone,
         'Date': selected_date,
         'Time': final_time}, ignore_index=1)

    print('Done')
    return email_df

