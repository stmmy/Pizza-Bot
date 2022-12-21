mport sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

print('Please answer the following questions: ')
time.sleep(1)


print('----Location----')
address = input('Address: ')
zip_code = str(input('Zip Code: '))
time.sleep(1)


#----------------------------------------------------------------------------


print('----Payment----')
card_num = input('Card #: ')
while True:
    exp_month_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    exp_month = input('Expiration Month(1 - 12): ')
    if exp_month in exp_month_list:
        break
    else:
        print('Invalid Month, Try Again')
while True:
    exp_year_list = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                            '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036']
    exp_year = input('Expiration Year (full year, ex. 2020): ')
    if exp_year in exp_year_list:
        break
    else:
        print('Invalid Year, Try Again')
sec_code = input('Security Code: ')
billing_zip_code = input('Billing Zip Code: ')
time.sleep(1)


#----------------------------------------------------------------------------


print('----Pizza Builder----')
while True:
    size_list = ['small', 'medium', 'large', 'x-large']
    size = input('Choose Size (small, medium, large, x-large): ')
    if size.lower() in size_list:
        break
    else:
        print('Invalid Size, Try Again')
while True:
    toppings_list = ['ham', 'beef', 'pepperoni', 'italian sausage', 'bacon',
                     'jalapeno peppers', 'onions', 'banana peppers',
                     'black olives', 'green olives', 'mushrooms',
                     'green peppers', 'roasted red peppers', 'none']
    topping1 = input('List of Toppings - \n\tham, beef, pepperoni, italian sausage, bacon, \n'
                     '\tjalapeno peppers, onions, banana peppers, \n'
                     '\tblack olives, green olives, mushrooms, \n'
                     '\tgreen peppers, roasted red peppers. \n'
                     'Topping #1 (if none, type none): ')
    if topping1.lower() in toppings_list:
        break
    else:
        print('Invalid Topping, Try Again')
while True:
    topping2 = input('Topping #2 (if none, type none): ')
    if topping2 in toppings_list:
        break
    else:
        print('Invalid Topping, Try Again')
while True:
    topping3 = input('Topping #3 (if none, type none): ')
    if topping3 in toppings_list:
        break
    else:
        print('Invalid Topping, Try Again')
while True:
    topping4 = input('Topping #4 (if none, type none): ')
    if topping4 in toppings_list:
        break
    else:
        print('Invalid Topping, Try Again')
time.sleep(1)


#----------------------------------------------------------------------------


driver = webdriver.Chrome()
driver.get("https://www.dominos.com/en/pages/order/#!/locations/search/")
#----------------------------------------------------------------------------
delivery = WebDriverWait(driver, 7).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="locationSearchForm"]/div/div[1]/label[1]/span[2]'))
)
delivery.click()
delivery.click()
delivery.click()
#----------------------------------------------------------------------------
street_address = driver.find_element_by_xpath('//*[@id="Street"]')
street_address.send_keys(str(address))
#----------------------------------------------------------------------------
online_zip_code = driver.find_element_by_id('Postal_Code_Sep')
online_zip_code.send_keys(str(zip_code))
#----------------------------------------------------------------------------
cont_delivery = driver.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[4]/button')
cont_delivery.click()
#----------------------------------------------------------------------------
build_pizza_start = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="entree-BuildYourOwn"]/a/div[2]/h2'))
)
build_pizza_start.click()


#----------------------------------------------------------------------------


if size.lower() == 'medium':
    medium_pizza = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="SizeCrustWrapper"]/div[4]/div/div[2]/label/span[2]'))
    )
    medium_pizza.click()
elif size.lower() == 'small':
    small_pizza = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="SizeCrustWrapper"]/div[4]/div/div[1]/label/span[2]'))
    )
    small_pizza.click()
elif size.lower() == 'large':
    large_pizza = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="SizeCrustWrapper"]/div[4]/div/div[3]/label/span[2]'))
    )
    large_pizza.click()
elif size.lower() == 'x-large':
    xlarge_pizza = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="SizeCrustWrapper"]/div[4]/div/div[4]/label/span[2]'))
    )
    xlarge_pizza.click()
else:
    print('Invalid')


#----------------------------------------------------------------------------


cheese_sauce = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button'))
)
cheese_sauce.click()
#----------------------------------------------------------------------------
toppings_button = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button'))
)
toppings_button.click()
#----------------------------------------------------------------------------
no_thanks = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="stepUpsell"]/div/button[1]'))
)
no_thanks.click()


#----------------------------------------------------------------------------


if topping1.lower() == 'ham':
    ham = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[1]/label/input'))
    )
    ham.click()
elif topping1.lower() == 'beef':
    beef = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[2]/label/input'))
    )
    beef.click()
elif topping1.lower() == 'pepperoni':
    pepperoni = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[4]/label/input'))
    )
    pepperoni.click()
elif topping1.lower() == 'italian sausage':
    italian_sausage = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[1]/label/input]'))
    )
    italian_sausage.click()
elif topping1.lower() == 'bacon':
    bacon = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[3]/label/input'))
    )
    bacon.click()
elif topping1.lower() == 'jalapeno peppers':
    jalapeno = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[2]/label/input'))
    )
    jalapeno.click()
elif topping1.lower() == 'onions':
    onions = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[3]/label/input'))
    )
    onions.click()
elif topping1.lower() == 'banana peppers':
    banana_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[4]/label/input'))
    )
    banana_peppers.click()
elif topping1.lower() == 'black olives':
    black_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[6]/label/input'))
    )
    black_olives.click()
elif topping1.lower() == 'green olives':
    green_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[7]/label/input'))
    )
    green_olives.click()
elif topping1.lower() == 'mushrooms':
    mushrooms = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]/label/input'))
    )
    mushrooms.click()
elif topping1.lower() == 'green peppers':
    green_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[4]/label/input'))
    )
    green_peppers.click()
elif topping1.lower() == 'roasted red peppers':
    roasted_red_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[6]/label/input'))
    )
    roasted_red_peppers.click()
else:
    print('error')


#----------------------------------------------------------------------------


if topping2.lower() == 'ham':
    ham = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[1]/label/input'))
    )
    ham.click()
elif topping2.lower() == 'beef':
    beef = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[2]/label/input'))
    )
    beef.click()
elif topping2.lower() == 'pepperoni':
    pepperoni = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[4]/label/input'))
    )
    pepperoni.click()
elif topping2.lower() == 'italian sausage':
    italian_sausage = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[1]/label/input]'))
    )
    italian_sausage.click()
elif topping2.lower() == 'bacon':
    bacon = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[3]/label/input'))
    )
    bacon.click()
elif topping2.lower() == 'jalapeno peppers':
    jalapeno = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[2]/label/input'))
    )
    jalapeno.click()
elif topping2.lower() == 'onions':
    onions = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[3]/label/input'))
    )
    onions.click()
elif topping2.lower() == 'banana peppers':
    banana_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[4]/label/input'))
    )
    banana_peppers.click()
elif topping2.lower() == 'black olives':
    black_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[6]/label/input'))
    )
    black_olives.click()
elif topping2.lower() == 'green olives':
    green_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[7]/label/input'))
    )
    green_olives.click()
elif topping2.lower() == 'mushrooms':
    mushrooms = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]/label/input'))
    )
    mushrooms.click()
elif topping2.lower() == 'green peppers':
    green_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[4]/label/input'))
    )
    green_peppers.click()
elif topping2.lower() == 'roasted red peppers':
    roasted_red_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[6]/label/input'))
    )
    roasted_red_peppers.click()
else:
    print('error')


#----------------------------------------------------------------------------


if topping3.lower() == 'ham':
    ham = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[1]/label/input'))
    )
    ham.click()
elif topping3.lower() == 'beef':
    beef = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[2]/label/input'))
    )
    beef.click()
elif topping3.lower() == 'pepperoni':
    pepperoni = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[4]/label/input'))
    )
    pepperoni.click()
elif topping3.lower() == 'italian sausage':
    italian_sausage = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[1]/label/input]'))
    )
    italian_sausage.click()
elif topping3.lower() == 'bacon':
    bacon = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[3]/label/input'))
    )
    bacon.click()
elif topping3.lower() == 'jalapeno peppers':
    jalapeno = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[2]/label/input'))
    )
    jalapeno.click()
elif topping3.lower() == 'onions':
    onions = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[3]/label/input'))
    )
    onions.click()
elif topping3.lower() == 'banana peppers':
    banana_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[4]/label/input'))
    )
    banana_peppers.click()
elif topping3.lower() == 'black olives':
    black_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[6]/label/input'))
    )
    black_olives.click()
elif topping3.lower() == 'green olives':
    green_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[7]/label/input'))
    )
    green_olives.click()
elif topping3.lower() == 'mushrooms':
    mushrooms = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]/label/input'))
    )
    mushrooms.click()
elif topping3.lower() == 'green peppers':
    green_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[4]/label/input'))
    )
    green_peppers.click()
elif topping3.lower() == 'roasted red peppers':
    roasted_red_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[6]/label/input'))
    )
    roasted_red_peppers.click()
else:
    print('error')


#----------------------------------------------------------------------------


if topping4.lower() == 'ham':
    ham = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[1]/label/input'))
    )
    ham.click()
elif topping4.lower() == 'beef':
    beef = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[2]/label/input'))
    )
    beef.click()
elif topping4.lower() == 'pepperoni':
    pepperoni = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[4]/label/input'))
    )
    pepperoni.click()
elif topping4.lower() == 'italian sausage':
    italian_sausage = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[1]/label/input]'))
    )
    italian_sausage.click()
elif topping4.lower() == 'bacon':
    bacon = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[3]/label/input'))
    )
    bacon.click()
elif topping4.lower() == 'jalapeno peppers':
    jalapeno = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[2]/label/input'))
    )
    jalapeno.click()
elif topping4.lower() == 'onions':
    onions = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[3]/label/input'))
    )
    onions.click()
elif topping4.lower() == 'banana peppers':
    banana_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[4]/label/input'))
    )
    banana_peppers.click()
elif topping4.lower() == 'black olives':
    black_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[6]/label/input'))
    )
    black_olives.click()
elif topping4.lower() == 'green olives':
    green_olives = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[7]/label/input'))
    )
    green_olives.click()
elif topping4.lower() == 'mushrooms':
    mushrooms = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]/label/input'))
    )
    mushrooms.click()
elif topping4.lower() == 'green peppers':
    green_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[4]/label/input'))
    )
    green_peppers.click()
elif topping4.lower() == 'roasted red peppers':
    roasted_red_peppers = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[2]/div[6]/label/input'))
    )
    roasted_red_peppers.click()
else:
    print('error')


#----------------------------------------------------------------------------


add_to_order = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button'))
)
add_to_order.click()
#----------------------------------------------------------------------------
pizza_sides_no_thanks = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="genericOverlay"]/section/header/button'))
)
pizza_sides_no_thanks.click()
#----------------------------------------------------------------------------
checkout = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="js-myOrderPage"]/a/span'))
)
checkout.click()
#----------------------------------------------------------------------------
no_go_to_checkout = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="genericOverlay"]/section/header/button'))
)
no_go_to_checkout.click()
WebDriverWait(driver, 3)
#----------------------------------------------------------------------------
continue_checkout = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="js-checkoutColumns"]/aside/div[3]/a'))
)
continue_checkout.click()
#----------------------------------------------------------------------------
#This will be temporary b/c of corona virus
got_it = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="_dpz"]/div[1]/section/div/div/div[2]/button'))
)
got_it.click()
#----------------------------------------------------------------------------
pay_now_with_card = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="orderPaymentPage"]/form/div[5]/div/div[2]/div/div[5]/label/input'))
)
pay_now_with_card.click()
#----------------------------------------------------------------------------
input_credit_card = driver.find_element_by_id('Credit_Card_Number')
input_credit_card.send_keys(str(card_num))
#----------------------------------------------------------------------------
input_security_code = driver.find_element_by_id('Credit_Card_Security_Code')
input_security_code.send_keys(str(sec_code))
#----------------------------------------------------------------------------
input_billing_zipcode = driver.find_element_by_id('Billing_Postal_Code')
input_billing_zipcode.send_keys(str(billing_zip_code))


#----------------------------------------------------------------------------


expiration_month = Select(driver.find_element_by_id('Expiration_Month'))
if exp_month == '1':
    expiration_month.select_by_value('1')
elif exp_month == '2':
    expiration_month.select_by_value('2')
elif exp_month == '3':
    expiration_month.select_by_value('3')
elif exp_month == '4':
    expiration_month.select_by_value('4')
elif exp_month == '5':
    expiration_month.select_by_value('5')
elif exp_month == '6':
    expiration_month.select_by_value('6')
elif exp_month == '7':
    expiration_month.select_by_value('7')
elif exp_month == '8':
    expiration_month.select_by_value('8')
elif exp_month == '9':
    expiration_month.select_by_value('9')
elif exp_month == '10':
    expiration_month.select_by_value('10')
elif exp_month == '11':
    expiration_month.select_by_value('11')
elif exp_month == '12':
    expiration_month.select_by_value('12')
else:
    print('error')


#----------------------------------------------------------------------------


expiration_year = Select(driver.find_element_by_id('Expiration_Year'))
if exp_year == '2020':
    expiration_year.select_by_value('2020')
elif exp_year == '2021':
    expiration_year.select_by_value('2021')
elif exp_year == '2022':
    expiration_year.select_by_value('2022')
elif exp_year == '2023':
    expiration_year.select_by_value('2023')
elif exp_year == '2024':
    expiration_year.select_by_value('2024')
elif exp_year == '2025':
    expiration_year.select_by_value('2025')
elif exp_year == '2026':
    expiration_year.select_by_value('2026')
elif exp_year == '2027':
    expiration_year.select_by_value('2027')
elif exp_year == '2028':
    expiration_year.select_by_value('2028')
elif exp_year == '2029':
    expiration_year.select_by_value('2029')
elif exp_year == '2030':
    expiration_year.select_by_value('2030')
elif exp_year == '2031':
    expiration_year.select_by_value('2031')
elif exp_year == '2032':
    expiration_year.select_by_value('2032')
elif exp_year == '2033':
    expiration_year.select_by_value('2033')
elif exp_year == '2034':
    expiration_year.select_by_value('2034')
elif exp_year == '2035':
    expiration_year.select_by_value('2035')
elif exp_year == '2036':
    expiration_year.select_by_value('2036')
else:
    print('error')


#----------------------------------------------------------------------------
