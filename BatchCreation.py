from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_signin():

    driver = webdriver.Chrome()
    driver.maximize_window()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


    driver.get("https://testing.testaonline.com/signin")

    try:

        email_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-email"))
        )
        email_id.send_keys("zaakefsotysvlrkopb@ckptr.com")

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-password"))
        )
        password.send_keys("SuperAdmin@1234")

        signin_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))
        )
        signin_button.click()


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Welcome back, Business Dashboard']"))
        )

        print("Signin Successful!")

        driver.get("https://testing.testaonline.com/exam-management/create-batch")

    #BatchDetails:

        batch_ID = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-batchId"))
        )
        batch_ID.send_keys("automatedTestBatch")

        batch_size = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-batchSize"))
        )
        batch_size.send_keys("10")

        Scheme_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-schemeId"))
        )
        Scheme_dd.click()

        schemedd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=':r1:']/li[2]"))
        )
        desired_option_text = "PMKVY-3.0-CSCMSP"
        for option in schemedd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break


        batch_start_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r3:"))
        )
        batch_start_date.send_keys("04-20-2024")

        batch_end_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r5:"))
        )
        batch_end_date.send_keys("04-26-2024")

        batch_start_time = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r8:"))
        )
        batch_start_time.send_keys("12:01 AM")

        batch_end_time = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":rb:"))
        )
        batch_end_time.send_keys("11:01 PM")

        batchmode_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-batchMode"))
        )
        batchmode_dd.click()

        batchmode_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=':r2o:']/li[2]"))
        )
        desired_option_text = "online"
        for option in batchmode_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

    ##Proctoring:

        Image_Proctoring_Time = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-imageProctoringTime"))
        )
        Image_Proctoring_Time.send_keys("1")

        Video_Duration = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-videoDuration"))
        )
        Video_Duration.send_keys("10")

        Video_Interval= WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-videoInterval"))
        )
        Video_Interval.send_keys("1")

        Max_wrong_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-noOfWrongLogin"))
        )
        Max_wrong_login.send_keys("2")

        NoofSuspicious_activity = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-noOfBrowserExit"))
        )
        NoofSuspicious_activity.send_keys("2")

    #Question paper

        Mark_review_Enable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='true'][name='markForReview']"))
                                              )
        if not Mark_review_Enable.is_selected():
            Mark_review_Enable.click()

        Question_Navigation_Enable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='true'][name='questionNavigation']"))
        )
        if not Question_Navigation_Enable.is_selected():
            Question_Navigation_Enable.click()

        Pagination_status_Enable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='true'][name='paginationStatus']"))
        )
        if not Pagination_status_Enable.is_selected():
            Pagination_status_Enable.click()

        Multilanguageexam_disable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='false'][name='examLanguageConduct']"))
        )
        if not Pagination_status_Enable.is_selected():
            Multilanguageexam_disable.click()

        JobRole = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "asynchronous-demo"))
        )
        JobRole.send_keys("DEVTESTer - Eaton Shepherd")

        JobLevel_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-level"))
        )
        JobLevel_dd.click()

        JobLevel_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":ro:"]/li[2]"))
        )
        desired_option_text = "4"
        for option in JobLevel_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        JobroleVersion_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-proctorId"))
        )
        JobroleVersion_dd .click()

        JobroleVersion_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":ro:"]/li[2]"))
        )
        desired_option_text = "2"
        for option in JobroleVersion_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        Instruction_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-chooseInstructions"))
        )
        Instruction_dd.click()

        Instruction_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rk:"]/li[2]"))
        )
        desired_option_text = "Assessment-1"
        for option in Instruction_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        Question_Set.send_keys("1")

        Passing_percent = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-passingPercentage"))
        )
        Passing_percent.send_keys("20")

        Theory_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='theory']"))
        )
        if not Theory_checkbox.is_selected():
            Theory_checkbox.click()

        Viva_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='viva']"))
        )
        if not Viva_checkbox.is_selected():
            Viva_checkbox.click()

        practical_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='practical']"))
        )
        if not practical_checkbox.is_selected():
            practical_checkbox.click()

        TheoryOrder_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-proctorId"))
        )
        TheoryOrder_dd.click()

        TheoryOrder_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rv:"]/li[4]"))
        )
        desired_option_text = "1"
        for option in TheoryOrder_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break
        Theory_Examduration = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-examDuration"))
        )
        Theory_Examduration.send_keys("20")

        VivaOrder_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-proctorId"))
        )
        VivaOrder_dd.click()

        VivaOrder_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rv:"]/li[4]"))
        )
        desired_option_text = "2"
        for option in VivaOrder_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        PracticalOrder_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-proctorId"))
        )
        PracticalOrder_dd.click()

        PracticalOrder_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rv:"]/li[4]"))
        )
        desired_option_text = "online"
        for option in PracticalOrder_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        AssessmentStatus_Enable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='true'][name='assesmentStatus']"))
        )
        if not AssessmentStatus_Enable.is_selected():
            AssessmentStatus_Enable.click()

        #Assign Assessor Proctor
        AssessorProctor_Enable = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='true'][name='assignAssessorProctor']"))
        )
        if not AssessorProctor_Enable.is_selected():
            AssessorProctor_Enable.click()

        Assessor_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-accessorId"))
        )
        Assessor_dd.click()
        Assessor_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rt:"]/li[2]"))
        )
        desired_option_text = "Imran Basha"
        for option in Assessor_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        Proctor_dd = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mui-component-select-proctorId"))
        )
        Proctor_dd.click()

        proctor_dd_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=":rv:"]/li[4]"))
        )
        desired_option_text = "online"
        for option in proctor_dd_options:
            if option.text.strip() == desired_option_text:
                option.click()
                break

        Finance_Remarks = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "outlined-adornment-financeRemarks"))
        )
        Finance_Remarks.send_keys("automated reamrks")


        # Click on the "Create Batch" button
        submit_batchform_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit']"))
        )
        submit_batchform_button.click()

        # Wait for success message or other confirmation
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=':r1:']"))
        )
        print("Batch created successfull")

    except Exception as e:
        print("An error occurred:", e)


    except Exception as e:
        print("An error occurred:", e)

    finally:

        driver.quit()


test_signin()

