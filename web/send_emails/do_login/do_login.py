from selenium.webdriver.common.by import By

from time import sleep


def do_login(driver, email, password):
    
    while len(driver.find_elements(By.XPATH, '//*[@id="lightbox-cover"]')) < 1:
        sleep(2)
    print("Login efetuado com sucesso.")
    sleep(2)
    
    user_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input')
    sleep(1)
    user_input.send_keys(email)
    sleep(1)
    forward_button = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
    sleep(1)
    forward_button.click()
    #

    sleep(4)    
    password_input = driver.find_element(By.XPATH, '//*[@id="i0118"]')
    sleep(1)
    password_input.send_keys(password)
    sleep(1)
    login_button = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
    sleep(0.5)
    login_button.click()
    sleep(20)
    forward_button_open = driver.find_element(By.XPATH, '//*[@id="iNext"]')
    sleep(2)
    forward_button_open.click()
    sleep(2)
    accept_button = driver.find_element(By.XPATH, '//*[@id="acceptButton"]')
    sleep(2)
    accept_button.click()   
    sleep(5)
    