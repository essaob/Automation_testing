import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Launch Chrome using undetected_chromedriver
# options = uc.ChromeOptions()
# options.add_argument("--start-maximized")
#
# driver = uc.Chrome(options=options)
# driver.get("https://www.yad2.co.il/")
# sleep(5)
#
# # Optional login section (currently commented out)
# # Email = driver.find_element(By.CLASS_NAME, 'direction-ltr')
# # Email.send_keys('alobraessa2212@gmail.com')
# # sleep(2)
# # User_pass = driver.find_element(By.ID, 'password')
# # User_pass.send_keys('your_password_here')
# # sleep(2)
# # Login = driver.find_element(By.ID, 'login-button')
# # Login.click()
# # sleep(5)
#
# # Click on an element by XPath (Hebrew alt text: 'כניסה')
# element = driver.find_element(By.XPATH, "//img[@alt='רכב']")
# element.click()
# sleep(3)
#
# elements = driver.find_elements(By.XPATH, "//img[@data-testid='image']")
# if len(elements)>0 :
#     print("ok , number the elemnts = ", len(elements))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yad2.co.il/")
    # sleep(40)
    yield driver
    driver.quit()


def test_Pagecar(driver):
    element = driver.find_element(By.XPATH, "//img[@alt='רכב']")
    element.click()
    sleep(3)

    elements = driver.find_elements(By.XPATH, "//img[@data-testid='image']")
    if len(elements) > 0:
        print("open page car , Successfully! , number the elemnts = ", len(elements))


# def test_history(driver):
#     sleep(20)
#
#     element = driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/header/div[4]/div/button")
#     element.click()
#     sleep(3)
#     elements = driver.find_elements(By.XPATH, "//*[@id='__next']/div[1]/div[1]/header/div[4]/section/ul[2]/li[3]/a/span[1]")
#     elements[1].click()
#     sleep(10)
#     # element.click()
#     # elements = driver.find_elements(By.XPATH, "//a[@data-v-5ff130d0='']")
#     # if len(elements) > 0:
#     #     print("History search , Successfully! , number the elemnts = ", len(elements))
#     #
#




#
# #################################################################################
# def test_yad2_click_first_business(driver):
#     driver.get("https://www.yad2.co.il/")
#     sleep(5)
#     driver.find_element(By.LINK_TEXT, "עסקים למכירה").click()
#     print("עבר לקטגוריית עסקים למכירה")
#     sleep(5)
#     driver.find_element(By.ID, "feed_item_0").click()
#     print("נפתחה המודעה הראשונה של עסק למכירה")
#     sleep(5)
#
# def test_yad2_click_last_business(driver):
#     driver.get("https://www.yad2.co.il/")
#     sleep(3)
#     driver.find_element(By.LINK_TEXT, "עסקים למכירה").click()
#     sleep(5)
#     last_business = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[2]/div[3]/div[last()]')
#     driver.execute_script("arguments[0].scrollIntoView();", last_business)
#     sleep(3)
#     last_business.click()
#     print("DONE - נלחצה המודעה האחרונה")
#     sleep(5)
#
# def test_yad2_click_last_page(driver):
#     driver.get("https://www.yad2.co.il/")
#     sleep(3)
#     driver.find_element(By.LINK_TEXT, "עסקים למכירה").click()
#     sleep(5)
#     pagination_block = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[2]/div[4]')
#     driver.execute_script("arguments[0].scrollIntoView();", pagination_block)
#     sleep(2)
#     page_buttons = pagination_block.find_elements(By.XPATH, ".//button[not(contains(text(), 'הבא')) and not(contains(text(), 'הקודם'))]")
#     if page_buttons:
#         last_button = page_buttons[-1]
#         print("לוחץ על עמוד: " + last_button.text)
#         ActionChains(driver).move_to_element(last_button).click().perform()
#     else:
#         print("לא נמצאו כפתורי עמודים")
#     sleep(5)
#
# def test_click_all_hearts(driver):
#     wait = WebDriverWait(driver, 15)
#     driver.get("https://www.yad2.co.il/")
#     wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "עסקים למכירה"))).click()
#     sleep(5)
#     added = set()
#     last_height = driver.execute_script("return document.body.scrollHeight")
#
#     while True:
#         heart_buttons = driver.find_elements(By.XPATH, "//button[@data-test-id='LIKE_AD']")
#         print("נמצאו " + str(len(heart_buttons)) + " מודעות במסך")
#
#         for btn in heart_buttons:
#             try:
#                 parent = btn.find_element(By.XPATH, "./ancestor::*[@id][contains(@id, 'feed_item_')]")
#                 item_id = parent.get_attribute("id")
#                 if item_id in added:
#                     continue
#                 ActionChains(driver).move_to_element(btn).click().perform()
#                 print("נוסף למועדפים: " + str(item_id))
#                 added.add(item_id)
#                 sleep(1)
#             except Exception as e:
#                 print("לא הצליח ללחוץ על לב: " + str(e))
#                 continue
#
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         sleep(3)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             print("סוף הרשימה - לא נטענו עוד מודעות")
#             break
#         last_height = new_height
#
# def test_yad2_filter_pets(driver):
#     driver.get("https://www.yad2.co.il/")
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "חיות מחמד"))).click()
#     sleep(4)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[2]/div[2]/div[2]/div[1]/button'))).click()
#     sleep(3)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[2]/div[2]/div[2]/div[2]/div/label[1]'))).click()
#     print("נבחרה תיבה: עם מחיר")
#     sleep(3)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/label[2]'))).click()
#     print("סינון בוצע")
#     sleep(5)
#
# def test_search_area(driver):
#     area_name = "דרום"
#     driver.get("https://www.yad2.co.il/")
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "עסקים למכירה"))).click()
#     sleep(5)
#     input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[1]/div/div/div[1]/div/label/span[3]/input')))
#     driver.execute_script("arguments[0].scrollIntoView();", input_box)
#     sleep(2)
#     input_box.clear()
#     input_box.send_keys(area_name)
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[1]/div/div'))).click()
#     print("נלחץ שוב על שדה הבחירה כדי לבחור את " + area_name)
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[normalize-space()='{area_name}']"))).click()
#     print("לחצנו על האפשרות המדויקת: " + area_name)
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[2]/div/div/div[3]/div/div/button[2]'))).click()
#     print("נלחץ על כפתור סינון אחרי הבחירה")
#     sleep(3)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/button'))).click()
#     print("בוצע חיפוש על אזור: " + area_name)
#     sleep(5)
#
# def test_filter_business_by_area_and_price(driver):
#     area_name = "דרום"
#     driver.get("https://www.yad2.co.il/")
#     wait = WebDriverWait(driver, 15)
#     wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "עסקים למכירה"))).click()
#     sleep(5)
#     input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[1]/div/div/div[1]/div/label/span[3]/input')))
#     driver.execute_script("arguments[0].scrollIntoView();", input_box)
#     sleep(2)
#     input_box.clear()
#     input_box.send_keys(area_name)
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[1]/div/div'))).click()
#     print("נלחץ שוב על שדה הבחירה כדי לבחור את " + area_name)
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[normalize-space()='{area_name}']"))).click()
#     print("לחצנו על האפשרות המדויקת: " + area_name)
#     sleep(2)
#     min_price_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[3]/div/div/div[1]/label/span[3]/input')))
#     driver.execute_script("arguments[0].scrollIntoView();", min_price_input)
#     sleep(1)
#     min_price_input.clear()
#     min_price_input.send_keys("200000")
#     print("נבחר מחיר מינימום: 200,000")
#     sleep(2)
#     max_price_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[3]/div/div/div[2]/label/span[3]/input')))
#     driver.execute_script("arguments[0].scrollIntoView();", max_price_input)
#     sleep(1)
#     max_price_input.clear()
#     max_price_input.send_keys("2000000")
#     print("נבחר מחיר מקסימום: 2,000,000")
#     sleep(2)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/ul/li[2]/div/div/div[3]/div/div/button[2]'))).click()
#     print("נלחץ על כפתור סינון אחרי הבחירה")
#     sleep(3)
#     wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div/div[4]/div[5]/div[1]/div/div[1]/div[1]/div/form/button'))).click()
#     ##################################################################################
#     #################
#     def test_1(driver):
#         login = driver.find_element(By.XPATH,
#                                     "//span[@class='profile-text_profileBoxText__SpcNt profile-text_showInMobile__Mn1Dv']")
#         login.click()
#         sleep(3)
#
#         input_email = driver.find_element(By.XPATH, "//input[@type='email']")
#         input_email.send_keys("u0091207@gmail.com")
#         sleep(2)
#         input_password = driver.find_element(By.XPATH, "//input[@type='password']")
#         input_password.send_keys("456780090")
#         sleep(3)
#
#         Login = driver.find_element(By.XPATH, "//button[@type='submit']")
#         Login.click()
#         sleep(3)
#
#         # ==================NEW USER=============================================>
#         new_user = driver.find_element(By.XPATH, "//a[@class='common-link']")
#         new_user.click()
#         sleep(4)
#         input_password = driver.find_element(By.XPATH, "//input[@id='password']")
#         input_password.send_keys("u456780090")
#         input_repassword = driver.find_element(By.XPATH, "//input[@id='re-entered-password']")
#         input_repassword.send_keys("u456780090")
#         sleep(3)
#         login_newuser = driver.find_element(By.XPATH, "//button[@type='submit']")
#         login_newuser.click()
#         sleep(3)
#
#
# def test_2_search(driver):
#     search = driver.find_element(By.XPATH, "//a[@href='/vehicles/cars']")
#     search.click()
#     sleep(5)
#     result_search= driver.find_elements(By.XPATH, "//div[@class='feed-item-content-box_feedItemContentBox__HEvdc']")
#     assert len(result_search)>1,"there is no results"
#     sleep(4)
#     Filter_cars= driver.find_element(By.XPATH, "//span[@class='desktop-only']")
#     Filter_cars.click()
#     sleep(2)
#     ClickCar=driver.find_element(By.XPATH, "//div[@class='icon-check-button_iconCheckButton__1nmqA']")
#     ClickCar.click()
#     sleep(3)
#     Facture=driver.find_element(By.XPATH, "//span[@class='rounded-pseudo-button_roundedPseudoButton__3fBVT pseudo-drop-button_pseudoDropButton__hYl0F']")
#     Facture.click()
#     sleep(2)
#     Facture_car=driver.find_element(By.XPATH, "//input[@placeholder='יצרן']")
#     Facture_car.click()
#     Facture_car.send_keys("אאודי")
#     sleep(2)
#     ResultsCar=driver.find_elements(By.XPATH, "//div[@class='options-list_optionsListBox__q4l4M']")
#     ShooseFirstCar=ResultsCar[0]
#     ShooseFirstCar.click()
#
#     Shoose_car=driver.find_element(By.XPATH, "//button[@id=':R16mkp6cmm:']")
#     Shoose_car.click()
#
#     #=====================================================דגם אוטו===================================
#
#     Shoose_car_felemnt=driver.find_element(By.XPATH, "//div[@class='vicon-check-item_textWrap__D8Bs_ vicon-check-item_default__nrg29']")
#     Shoose_car_felemnt.click()
#     sleep(3)
#
#
#     #=====================================================years===================================
#     car_Year=driver.find_element(By.XPATH, "//button[@id=':R8mkp6cmm:']")
#     car_Year.click()
#     sleep(3)
#     Dr_elements = driver.find_elements(By.XPATH,"//span[@class='pseudo-button_pseudoButton__QkXDZ pseudo-drop-button_pseudoDropButton__hYl0F']")
#     Dr_elements[0].click()
#     Elements = driver.find_elements(By.XPATH, "//div[@class='vicon-check-item_textWrap__D8Bs_ vicon-check-item_default__nrg29']")
#
#     for item in Elements:
#         Year = item.find_element(By.XPATH, ".//span")
#         if Year.text == '2023':
#             Year.click()
#             break
#
#     sleep(3)
#     Dr_elements[1].click()
#     Elements_ToYear = driver.find_elements(By.XPATH, "//div[@class='vicon-check-item_textWrap__D8Bs_ vicon-check-item_default__nrg29']")
#
#     for Item in Elements_ToYear:
#         ToYear = Item.find_element(By.XPATH, ".//span")
#         if ToYear.text == '2025':
#             ToYear.click()
#             break
#     sleep(3)
#     #=============================Filters=============================================================
#
#     driver.find_element(By.XPATH,
#                         "//span[@class='rounded-pseudo-button_roundedPseudoButton__3fBVT toggle-button_toggleButtonBox__7_T_5']").click()
#     sleep(3)
#     Area_element= driver.find_elements(By.XPATH, "//div[@class='ad-characteristics-layout_checkboxesGroupBox__LYWL9']")
#     Area_element[0].click()
#     sleep(3)
#     Filter_car = driver.find_element(By.XPATH, "//input[@type='text']")
#     Filter_car.click()
#     sleep(3)
#     Filter_car.send_keys(9000)
#     sleep(3)
#     Filter_car2 = driver.find_element(By.XPATH, "//input[@placeholder='800']")
#     Filter_car2.click()
#     sleep(3)
#     Filter_car2.send_keys(2300)
#     sleep(4)
#
#     usedBy=driver.find_element(By.XPATH, "//button[@class='buttons-range_button__hNTr6']")
#     usedBy.click()
#     sleep(3)
#     area = driver.find_element(By.XPATH, "//button[@id=':R2daqmkp6cmm:']")
#     area.click()
#     sleep(3)
#     list_area = driver.find_element(By.XPATH, "//button[@class='group-dropdown_headerTitle__L_Fma']")
#     list_area.click()
#     sleep(3)
#     groupOfList = driver.find_elements(By.XPATH,
#                                        "//div[@class='vicon-check-item_textWrap__D8Bs_ vicon-check-item_orange__1OP4d']")
#     groupOfList[2].click()
#     sleep(3)
#
# def test_3_Filters(driver):
#     driver.find_element(By.LINK_TEXT,"נדל״ן").click()
#     sleep(5)
#     input_area=driver.find_element(By.XPATH, "//input[@aria-autocomplete='list']")
#     input_area.send_keys("באר שבע ")
#     sleep(4)
#     beer7_area=driver.find_element(By.XPATH, "//span[@class='pseudo-drop-button_text__duTa4']")
#     beer7_area.click()
#     sleep(3)
#     beer7salt_area=driver.find_element(By.XPATH, "//a[@class='transaction-type_button__37ulL']")
#     beer7salt_area.click()
#     sleep(4)
#     #=================================================סוג הנכס===============================================
#     property_type = driver.find_element(By.XPATH, "//span[@aria-label='סוג הנכס']")
#     property_type.click()
#     sleep(3)
#     Apartments = driver.find_elements(By.XPATH, "//span[@class='simple-check-button_simpleButton__UmBDB']")
#     Apartments[17].click()
#     sleep(3)
#     #========================================================מחיר=================================================
#     price=driver.find_elements(By.XPATH, "//div[@class='responsive-dropdown_responsiveDropdownBox__646lN']")
#     for i in price:
#         pric=i.find_element(By.XPATH, ".//span")
#         if pric.text=="מחיר":
#             pric.click()
#             break
#     sleep(3)
#     shoose_price=driver.find_element(By.XPATH, "//input[@class='simple-input_simpleInput__WPLhX inputs-slider-range_input__fZs4Z']")
#     shoose_price.click()
#     sleep(1)
#     shoose_price.send_keys("300000")
#     sleep(3)
#     for rooms in price:
#         room=rooms.find_element(By.XPATH, ".//span")
#         if room.text=="חדרים":
#             room.click()
#             break
#     sleep(3)
#     NumOfRooms=driver.find_element(By.XPATH, "//div[@class='buttons-range_buttonsRangeBox__VCTmF']")
#     NumOfRooms.click()
#     sleep(3)
#
#     Filters_ndln=driver.find_element(By.XPATH, "//span[@class='rounded-pseudo-button_roundedPseudoButton__3fBVT toggle-button_toggleButtonBox__7_T_5']")
#     Filters_ndln.click()
#     sleep(6)
#     features_room=driver.find_elements(By.XPATH, "//span[@class='check-box_title__i76lj']")
#     features_room[2].click()
#     features_room[4].click()
#     sleep(6)
#     Advertiser = driver.find_elements(By.XPATH, "//div[@class='icon-check-button_iconCheckButton__yis__']")
#     Advertiser[3].click()
#     sleep(3)
#     features_room[8].click()
#     sleep(3)
#     Floors= driver.find_element(By.XPATH, "//div[@class='base-select_select__BYmkn']")
#     Floors.click()
#     sleep(3)
#     NumOfFloor=driver.find_elements(By.XPATH, "//div[@class='container_item__c7jvh']")
#     for number in NumOfFloor:
#         numroom=number.find_element(By.XPATH, ".//span")
#         if numroom.text == "2":
#             numroom.click()
#             break
#     sleep(4)
#     Floors.click()
#
# #===========================================Filters=========================================================
#
#     date=driver.find_element(By.XPATH, "//div[@class='text-field_box__OSyqV text-field_flexed__IDcF9 text-field_grey__M2DPM text-field_default-size-small__jUD6R']")
#     date.click()
#     sleep(3)
#     Calendar = driver.find_element(By.XPATH, "//input[@data-testid='text-field-undefined']")
#     driver.execute_script("arguments[0].value = arguments[1];", Calendar, "2025-04-28")
#     sleep(3)
#     registration=driver.find_element(By.XPATH, "//div[@class='checkbox_y2Checkbox__kIaBN checkbox_center__L__6m']")
#     registration.click()
#     sleep(1)
#     Approval=driver.find_element(By.XPATH, "//button[@class='action-buttons_approve__pG6HF']")
#     Approval.click()
#     sleep(4)
#     SEARCH=driver.find_element(By.XPATH, "//button[@class='button_button__KrRYB button_flexed__XqvBS button_default-primary__FFbtC button_default-size-small__xx_BR form-action-box_submitButton__YZDcr']")
#     SEARCH.click()
#     sleep(4)
