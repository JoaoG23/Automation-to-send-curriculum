from selenium.webdriver.common.by import By

from time import sleep

from send_emails.get_text_from_file.get_text_from_file import get_text_from_file


def add_footer(driver, sequence_id_body):
    get_text_from_file("templates/footer.txt")
    sleep(2)
    body_textarea = driver.find_element(By.XPATH, f'//*[@id="editorParent_{sequence_id_body}"]/div')
    sleep(1)
    body_textarea.send_keys("""
                            
Atenciosamente,
João Guilherme Tito de Jesus
Tel: (31) 99621-6938 
""")